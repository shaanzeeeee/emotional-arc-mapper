# 🎬 Emotional Arc Mapper

**Emotional Arc Mapper** is an end-to-end AI/ML application that visualizes the "emotional temperature" of films and TV shows. By leveraging state-of-the-art Natural Language Processing (NLP), the tool parses movie scripts or subtitles and maps the narrative journey into a time-series emotional valence chart.

---

## 🚀 Key Features
- **Transformer-based Sentiment Analysis**: Utilizes `RoBERTa` (via HuggingFace) for high-accuracy sentiment detection.
- **Narrative Time-Series Visualization**: Automatically converts raw dialogue into a smoothed emotional arc.
- **Support for Multiple Formats**: Effortlessly parses `.srt` (subtitles) and `.txt` (screenplays).
- **Interactive Dashboard**: Built with **Streamlit** and **Plotly** for real-time exploratory data analysis.
- **Moment Inspection**: Interactively explore specific dialogue lines by clicking on data points in the emotional arc.

---

## 🛠️ Technology Stack
- **NLP Engine**: HuggingFace Transformers, RoBERTa (`cardiffnlp/twitter-roberta-base-sentiment-latest`)
- **Data Engineering**: Pandas, NumPy, re (Regex)
- **Frontend/UX**: Streamlit
- **Visualization**: Plotly Express
- **Automation**: Git, Git LFS (for large models)

---

## 🏗️ Technical Architecture
```mermaid
graph TD
    A[Raw Script/Subtitle File] --> B[Script Parser (pysrt/Regex)]
    B --> C[Text Normalization & Tokenization]
    C --> D[Sentiment Engine (RoBERTa Transformer)]
    D --> E[Time-Series Valence Mapping]
    E --> F[Smoothing Filter (Rolling Average)]
    F --> G[Interactive UI (Streamlit/Plotly)]
```

---

## ⚙️ Installation & Setup

### 1. Prerequisite
- Python 3.9+
- [Git](https://git-scm.com/)

### 2. Physical Setup
```bash
# Clone the repository
git clone https://github.com/shaanzeeeee/emotional-arc-mapper.git
cd emotional-arc-mapper

# Create and activate virtual environment
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## 📖 Usage
To launch the interactive dashboard, run:
```bash
python -m streamlit run src/app.py
```

1. Upload an `.srt` or `.txt` file in the sidebar.
2. Click **"Run Analytics"**.
3. Explore the emotional trajectory of your favorite story!

---

## 💡 Resume Insights
This project demonstrates expertise in:
- **Large-scale Unstructured Data Processing**: Handling and cleaning thousands of lines of narrative text.
- **Modern Transformer Architectures**: Implementing pre-trained BERT/RoBERTa models for downstream tasks.
- **Full-Stack ML Engineering**: Bridging the gap between a raw model and an interactive user interface.
- **Data Storytelling**: Visualizing complex emotional data to provide actionable narrative insights.

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
