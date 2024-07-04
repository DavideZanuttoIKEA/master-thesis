import json

# Define the path to the input TXT file and the output JSON file
input_file_path = 'external_datasets/ext_sick/SICK.txt'
output_file_path = 'external_datasets/ext_sick/scores.json'

# Initialize an empty list to store the heights
scores = []

# Read data from the file
with open(input_file_path, 'r') as file:
    # Skip the header line
    next(file)
    for line in file:
        # Split the line into components based on commas
        parts = line.strip().split('\t')
        # The height is the third element, convert it to float and append to the list
        try:
            score = float(parts[4])
            scores.append(score)
        except ValueError:
            # Handle the case where conversion to float fails
            print(f"Skipping invalid data: {parts[4]}")

# Write the list of heights to a JSON file
with open(output_file_path, 'w') as json_file:
    json.dump(scores, json_file)

print("Scores extracted and written to JSON file successfully.")
