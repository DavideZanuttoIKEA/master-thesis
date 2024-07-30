import os
import csv

def process_centroids_folder(folder_path, output_csv):
    # Ensure the folder exists
    if not os.path.exists(folder_path):
        print(f"Folder {folder_path} does not exist.")
        return
    
    # Prepare to write to a CSV file
    with open(output_csv, 'w', newline='') as csvfile:
        fieldnames = ['art_id', 'core_keyphrases']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        # Process each file in the directory
        for filename in os.listdir(folder_path):
            if filename.startswith("embeddings_") and filename.endswith("_closest_keyphrases.txt"):
                # Extract art_id from the filename
                art_id = filename[len("embeddings_"):-len(".csv.pkl_closest_keyphrases.txt")]
                
                # Read keyphrases from the file
                keyphrases_path = os.path.join(folder_path, filename)
                with open(keyphrases_path, 'r') as file:
                    keyphrases = file.read().strip()
                
                # Write the data to the CSV file
                writer.writerow({'art_id': art_id, 'core_keyphrases': keyphrases})

# Path to the folder containing the keyphrases files
centroids_folder = "../centroids"
# Path to the output CSV file
output_csv_path = "core_keyphrases_hierarchical.csv"

process_centroids_folder(centroids_folder, output_csv_path)