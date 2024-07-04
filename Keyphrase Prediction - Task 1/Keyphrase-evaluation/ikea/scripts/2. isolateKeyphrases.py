import pandas as pd

def clean_csv_data(input_csv_path, output_csv_path):
    # Read the CSV file
    data = pd.read_csv(input_csv_path)
    
    # Function to remove text after dash in each cell
    def remove_after_dash(text):
        # Check if the input is a string to avoid errors with non-string data
        if isinstance(text, str):
            # Split the string at each dash and join back without the parts after each dash
            return ', '.join(part.split(' - ')[0] for part in text.split(', '))
        return text

    # Apply the function to each element in the DataFrame
    cleaned_data = data.applymap(remove_after_dash)
    
    # Save the cleaned DataFrame to a new CSV file
    cleaned_data.to_csv(output_csv_path, sep=';', index=False)

# Example usage
input_csv_path = 'ikea/merged/llama-instruct-finetuned-rslora_merged.csv'
output_csv_path = 'ikea/preprocessed/llama-instruct-finetuned-rslora.csv'
clean_csv_data(input_csv_path, output_csv_path)
print(f"Data cleaned and saved to {output_csv_path}")
