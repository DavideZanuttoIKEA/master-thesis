import pandas as pd

file_path = 'artID+reviews.csv' 
data = pd.read_csv(file_path)

original_count = len(data)
print(f"Original number of reviews: {original_count}")

data_cleaned = data.drop_duplicates(subset=['Reviews'], keep='first')

cleaned_count = len(data_cleaned)
print(f"Number of reviews after removing duplicates: {cleaned_count}")

output_file_path = 'new.csv' 
data_cleaned.to_csv(output_file_path, index=False, sep=";")

print(f"Cleaned data saved to {output_file_path}")
