from transformers import pipeline
import pandas as pd
import numpy as np

class SentimentEngine:
    def __init__(self, model_name="cardiffnlp/twitter-roberta-base-sentiment-latest"):
        """Initializes the sentiment analysis pipeline."""
        print(f"Loading model: {model_name}...")
        self.analyzer = pipeline("sentiment-analysis", model=model_name, tokenizer=model_name)
        self.label_map = {
            "negative": -1,
            "neutral": 0,
            "positive": 1
        }

    def analyze_text(self, text):
        """Returns a sentiment score between -1 and 1."""
        try:
            # Handle empty or very short text
            if not text or len(text.strip()) < 2:
                return 0
                
            result = self.analyzer(text[:512])[0] # Truncate to 512 for BERT limits
            label = result['label'].lower()
            score = result['score']
            
            # Weighted valence: label direction * confidence score
            valence = self.label_map.get(label, 0) * score
            return valence
        except Exception as e:
            print(f"Error analyzing text: {e}")
            return 0

    def process_dataframe(self, df):
        """Processes a dataframe with a 'text' column and adds a 'sentiment' column."""
        print("Processing sentiment analysis...")
        df['sentiment'] = df['text'].apply(self.analyze_text)
        
        # Calculate a rolling average for smoothness
        df['sentiment_smooth'] = df['sentiment'].rolling(window=10, min_periods=1, center=True).mean()
        
        return df

if __name__ == "__main__":
    # Test block
    engine = SentimentEngine()
    test_text = "I love this movie! It is so uplifting and happy."
    print(f"Test Score: {engine.analyze_text(test_text)}")
