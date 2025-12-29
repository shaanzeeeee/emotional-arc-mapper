import streamlit as st
import pandas as pd
import plotly.express as px
import os
from parser import parse_srt, parse_txt
from engine import SentimentEngine

# Page Config
st.set_page_config(page_title="Emotional Arc Mapper", layout="wide")

st.title("🎬 Emotional Arc Mapper")
st.markdown("Visualize the emotional journey of your favorite movie or TV show.")

# Initialize Engine (cached to avoid reloading model)
@st.cache_resource
def load_engine():
    return SentimentEngine()

engine = load_engine()

# Sidebar: File Upload
st.sidebar.header("Settings")
uploaded_file = st.sidebar.file_uploader("Upload Subtitle (.srt) or Script (.txt)", type=["srt", "txt"])

if uploaded_file is not None:
    # Ensure data directory exists
    if not os.path.exists("data"):
        os.makedirs("data")
        
    # Save temp file
    temp_path = os.path.join("data", uploaded_file.name)
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.info(f"Processing '{uploaded_file.name}'...")
    
    # 1. Parse
    if uploaded_file.name.endswith(".srt"):
        df = parse_srt(temp_path)
    else:
        df = parse_txt(temp_path)
        
    # 2. Analyze
    if st.sidebar.button("Run Analytics"):
        with st.spinner("Analyzing sentiments (this may take a while)..."):
            df = engine.process_dataframe(df)
            
            # 3. Visualize
            st.subheader("📊 Emotional Arc")
            fig = px.line(df, x="timestamp", y="sentiment_smooth", 
                          title=f"Emotional Valence Over Time: {uploaded_file.name}",
                          labels={"timestamp": "Time (Seconds/Line)", "sentiment_smooth": "Emotional Valence"},
                          hover_data=["text"])
            
            # Styling
            fig.update_traces(line_color='#e74c3c', line_width=2)
            fig.add_hline(y=0, line_dash="dash", line_color="gray", annotation_text="Neutral")
            
            st.plotly_chart(fig, use_container_width=True)
            
            # 4. Data View
            with st.expander("View Raw Data"):
                st.dataframe(df)
            
            st.success("Analysis Complete!")
else:
    st.warning("Please upload a file in the sidebar to begin.")
    st.markdown("""
    ### How it works:
    1. **Upload** an .srt or .txt file of a movie script.
    2. The system **Parses** the dialogue and timestamps.
    3. Our **Transformer Model** analyzes the emotion of every line.
    4. A **Smooth Graph** is generated showing the 'Emotional Temperature' of the story.
    """)
