import csv
import json

# Define the path to the source text file and the output JSON file
input_path = 'ikea/preprocessed/llama-instruct-finetuned-rslora.csv'
output_path = 'model_outputs/ikea/llama-instruct-finetuned-rslora/ikea_hypotheses_linked.json'

# Function to map from one range to another (assumed from 1 to 5 to 0 to 1)
def map_range(value, from_min, from_max, to_min, to_max):
    from_span = from_max - from_min
    to_span = to_max - to_min
    value_scaled = float(value - from_min) / float(from_span)
    return to_min + (value_scaled * to_span)

# Initialize min and max score values assuming scores are between 1 and 5
# min_score, max_score = 0, 5

with open(input_path, 'r', newline='', encoding='utf-8') as file, open(output_path, 'w', encoding='utf-8') as jsonfile:
    reader = csv.DictReader(file, delimiter=';')    
      
    if reader.fieldnames:
        # Verify the indices are within the range of columns available
        if len(reader.fieldnames) < max([0,1]):
            raise ValueError("Not enough columns in the input file.")
        fieldnames = [reader.fieldnames[0], reader.fieldnames[1]]  # Adjust indices according to actual content
        
    else:
        raise ValueError("No columns found in the input file.")
    
    for row in reader:
           
        # Map the score from column 4
        # mapped_score = map_range(float(row[fieldnames[2]]), min_score, max_score, 0, 1)
        selected_row = {
            "source": "a",
            "target": row[fieldnames[0]],
            "predictions": row[fieldnames[1]]
        }

        jsonfile.write(json.dumps(selected_row) + '\n')


print(f"Data has been written to {output_path}")

"""
# Print examples of original scores and their mapped values
print("\nExamples of Original and Mapped Scores (First 10 entries):")
for item in data[:10]:
    print(f"Original: {item['score'] * 4 + 1}, Mapped: {item['score']}")"""