import pandas as pd
import re

# Load the CSV file
df = pd.read_csv("sample_data.csv")

# Function to clean Hindi-English mixed text
def clean_mixed_text(text):
    # Remove emojis and special symbols (keeping only Hindi, English, numbers, basic punctuation)
    text = re.sub(r"[^\w\s\u0900-\u097F.,!?]", "", text)

    # Normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text

# Apply the cleaning function to the text column
df['cleaned_text'] = df['text'].astype(str).apply(clean_mixed_text)

# Save to cleaned CSV
df.to_csv("cleaned_data.csv", index=False)

print("✅ Text cleaning completed. Cleaned data saved to 'cleaned_data.csv'")
