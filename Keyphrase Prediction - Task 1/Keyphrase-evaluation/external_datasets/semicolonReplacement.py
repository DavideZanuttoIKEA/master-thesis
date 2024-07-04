input_path = 'model_outputs/tsv_semEval2014/human/tsv_semEval2014_hypotheses_linked.json'
output_path = 'model_outputs/tsv_semEval2014/human/tsv_semEval2014_hypotheses_linked.json'

# Read the JSON file into a string
with open(input_path, 'r', encoding='utf-8') as file:
    file_contents = file.read()

# Replace all semicolons in the string
modified_contents = file_contents.replace(';', ',')

# Write the modified string back to a new JSON file
with open(output_path, 'w', encoding='utf-8') as file:
    file.write(modified_contents)

print(f"All semicolons have been removed from {input_path} and the result has been saved to {output_path}.")
