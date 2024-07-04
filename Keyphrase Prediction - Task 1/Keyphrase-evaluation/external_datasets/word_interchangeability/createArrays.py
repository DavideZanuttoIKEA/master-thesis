import pandas as pd

# Load the CSV file
df = pd.read_csv('external_datasets/word_interchangeability/win353.csv', header=None)  # Adjust the path to where your CSV file is stored

# Extract columns into lists
first_column = df[0].tolist()
second_column = df[1].tolist()

# Printing the results
print("First Column:", first_column)
print("Second Column:", second_column)