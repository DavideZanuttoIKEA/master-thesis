import csv

def process_txt_to_csv(input_txt_file, output_csv_file):
    with open(input_txt_file, 'r') as infile, open(output_csv_file, 'w', newline='') as outfile:
        csv_writer = csv.writer(outfile)
        csv_writer.writerow(['art_id', 'core keyphrases'])  # Writing the header of the CSV

        for line in infile:
            if ':' in line:  # Ensure there is a keyphrase part in the line
                # Splitting on the first colon found
                part_id, keyphrases = line.split(':', 1)
                # Extract the numerical art_id from the part identifier (e.g., "embeddings_89386107.csv.pkl")
                art_id = part_id.split('_')[1].split('.')[0]
                # Cleaning up keyphrases (removing newlines and extra spaces)
                keyphrases = keyphrases.strip().replace('\n', '')
                # Write to CSV
                csv_writer.writerow([art_id, keyphrases])

# Example usage:
input_txt_file = 'keyphrases_by_product.txt'
output_csv_file = 'core_keyphrases.csv'
process_txt_to_csv(input_txt_file, output_csv_file)