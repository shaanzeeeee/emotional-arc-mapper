import pysrt
import pandas as pd
import re

def parse_srt(file_path):
    """Parses an .srt file and returns a list of dictionaries with text and timestamps."""
    subs = pysrt.open(file_path, encoding='iso-8859-1')
    data = []
    for sub in subs:
        # Calculate mid-point time in seconds
        start_secs = (sub.start.hours * 3600 + sub.start.minutes * 60 + sub.start.seconds + sub.start.milliseconds / 1000)
        end_secs = (sub.end.hours * 3600 + sub.end.minutes * 60 + sub.end.seconds + sub.end.milliseconds / 1000)
        mid_time = (start_secs + end_secs) / 2
        
        # Clean text
        text = sub.text.replace('\n', ' ')
        text = re.sub(r'<[^>]*>', '', text) # Remove HTML tags
        
        data.append({
            'timestamp': mid_time,
            'text': text
        })
    return pd.DataFrame(data)

def parse_txt(file_path):
    """Simple parser for plain text scripts (no timestamps)."""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Filter out empty lines
    lines = [line.strip() for line in lines if line.strip()]
    
    # Since there are no timestamps, we assign artificial ones (line index)
    data = [{'timestamp': i, 'text': line} for i, line in enumerate(lines)]
    return pd.DataFrame(data)

if __name__ == "__main__":
    # Example usage (can be tested later with a real file)
    print("Parser module ready.")
