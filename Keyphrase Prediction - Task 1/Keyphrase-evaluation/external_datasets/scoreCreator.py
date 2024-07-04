import csv
import json

# Define the path to the source TSV file and the output JSON file
input_path = 'external_datasets/domain-specific/Book1.csv'
output_path = 'external_datasets/domain-specific/Book1-scores.json'

# Function to map scores from 0-5 scale to 0-1 scale
def map_range(value, from_min=0, from_max=1, to_min=0, to_max=1):
    from_span = from_max - from_min
    to_span = to_max - to_min
    value_scaled = float(value - from_min) / float(from_span)
    return to_min + (value_scaled * to_span)

# List to hold the mapped scores
mapped_scores = []

# Read the TSV file and process scores
with open(input_path, 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=',')
    next(reader)  # Skip header row if there is one; remove this line if there isn't a header
    for row in reader:
        if row:  # Checking if the row is not empty
            original_score = float(row[2])  # Convert the first column to float
            mapped_score = map_range(original_score)  # Map the score
            mapped_scores.append(mapped_score)

# Write the mapped scores to a JSON file
with open(output_path, 'w', encoding='utf-8') as jsonfile:
    json.dump(mapped_scores, jsonfile, indent=4)

print(f"Mapped scores have been written to {output_path}")