import pandas as pd

# Load the CSV file
file_path = 'artID+reviews.csv'  # Update this to your CSV file path
data = pd.read_csv(file_path)

# Check how many rows are in the original data
original_count = len(data)
print(f"Original number of reviews: {original_count}")

# Remove duplicates based on the 'Review' column
# keep='first' keeps the first occurrence and removes other duplicates
data_cleaned = data.drop_duplicates(subset=['Reviews'], keep='first')

# Check how many rows are in the data after removing duplicates
cleaned_count = len(data_cleaned)
print(f"Number of reviews after removing duplicates: {cleaned_count}")

# Save the cleaned data back to CSV
output_file_path = 'new.csv'  # Update this to your desired output file path
data_cleaned.to_csv(output_file_path, index=False, sep=";")

print(f"Cleaned data saved to {output_file_path}")
