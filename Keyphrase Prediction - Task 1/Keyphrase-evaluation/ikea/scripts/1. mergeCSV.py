import pandas as pd
import openpyxl

def merge_files_and_save(csv_file_path, xlsx_file_path, output_csv_path):
    # Read the second column from the CSV file
    csv_data = pd.read_csv(csv_file_path, usecols=[1], header=0, sep=";")
    csv_data.columns = ['LLM']  # Rename the column for clarity

    # Read the second column from the XLSX file
    xlsx_data = pd.read_excel(xlsx_file_path, usecols=[1], header=0)
    xlsx_data.columns = ['Ground truth']  # Rename the column for clarity

    # Merge the two dataframes with specified column order for output
    merged_data = pd.concat([xlsx_data, csv_data], axis=1)
    # Save the merged DataFrame to a new CSV file
    merged_data.to_csv(output_csv_path, index=False)

# Example usage
csv_file_path = 'ikea/llama-instruct-finetuned-rslora.csv'
xlsx_file_path = 'ikea/cleaned_evaluation_keyphrases_200US.xlsx'
output_csv_path = 'ikea/merged/llama-instruct-finetuned-rslora_merged.csv'
merge_files_and_save(csv_file_path, xlsx_file_path, output_csv_path)
print(f"Merged data saved to {output_csv_path}")
