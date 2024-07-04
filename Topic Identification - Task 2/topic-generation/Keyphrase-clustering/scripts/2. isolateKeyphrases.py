import pandas as pd
import os

def clean_keyphrases(input_csv, output_csv):
    df = pd.read_csv(input_csv)

    if 'Keyphrases' not in df.columns:
        raise ValueError("The CSV file does not have a 'Keyphrases' column.")

    def clean_text(text):
        return ", ".join([phrase.strip().split(' -')[0] for phrase in text.split(',')])

    df['Keyphrases'] = df['Keyphrases'].apply(clean_text)
    df.to_csv(output_csv, index=False)
    print(f"Cleaned data saved to {output_csv}")

def process_folder(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.csv'):
            input_csv = os.path.join(input_folder, filename)
            output_csv = os.path.join(output_folder, filename)
            try:
                clean_keyphrases(input_csv, output_csv)
            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Example usage: Specify the input and output directories
process_folder('articles', 'cleaned_articles')
