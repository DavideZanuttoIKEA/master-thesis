import pandas as pd
import os

def merge_tsv_files(directory_path, output_file):
    """
    Merges all TSV files in the given directory into a single TSV file.
    
    Args:
    directory_path (str): The path to the directory containing the TSV files.
    output_file (str): The path where the merged TSV file will be saved.
    """
    # Initialize an empty list to store the dataframes
    df_list = []

    # Loop through all files in the specified directory
    for filename in os.listdir(directory_path):
        if filename.endswith('.tsv'):
            file_path = os.path.join(directory_path, filename)
            # Read the current TSV file into a dataframe
            df = pd.read_csv(file_path, delimiter='\t')
            # Append the dataframe to our list
            df_list.append(df)

    # Concatenate all dataframes in the list into a single dataframe
    merged_df = pd.concat(df_list, ignore_index=True)

    # Write the merged dataframe to a new TSV file
    merged_df.to_csv(output_file, sep='\t', index=False)

    print(f"Merged {len(df_list)} files into {output_file}")

# Example usage
directory_path = 'external_datasets/tsv_semEval2012'
output_file = 'external_datasets/tsv_semEval2012/semEval2012.tsv'
merge_tsv_files(directory_path, output_file)
