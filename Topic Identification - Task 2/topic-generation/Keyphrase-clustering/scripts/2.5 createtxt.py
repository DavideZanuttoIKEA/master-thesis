import csv
import os

# Path to your CSV file
input_folder = 'cleaned_articles'
output_folder = 'keyphrases_txt'

for filename in os.listdir(input_folder):
    if filename.endswith('.csv'):
        input_csv = os.path.join(input_folder, filename)
        output_csv = os.path.join(output_folder, filename)
        # List to hold all unique keyphrases
        keyphrases = []

        # Read the CSV file
        with open(input_csv, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Assuming the column containing the keyphrases is named 'Keyphrases'
                # Split the keyphrases on comma and strip any surrounding whitespace
                phrases = [phrase.strip() for phrase in row['Keyphrases'].split(',')]
                keyphrases.extend(phrases)

        # Optionally, remove duplicates by converting list to a set and back to a list
        keyphrases = list(set(keyphrases))

        with open(f'{filename}.txt', 'w', encoding='utf-8') as f:
            for phrase in keyphrases:
                f.write(f"{phrase}\n")

        # Output the list of keyphrases
        print(keyphrases)
