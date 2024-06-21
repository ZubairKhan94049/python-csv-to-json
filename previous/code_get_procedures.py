import pandas as pd
import re

# Read the CSV file
file_path = 'procedure_data.csv'
df = pd.read_csv(file_path)

# Extract the 'Procedure Title' column
procedure_titles = df['Procedure Title']

# Remove words after 'cost' and 'cost' itself
procedure_titles = procedure_titles.str.extract(r'^(.*?)\s*cost', flags=re.IGNORECASE)[0]

# Remove duplicates
procedure_titles = procedure_titles.drop_duplicates()

# Save to a .txt file
output_file_path = 'extracted_procedure_titles.txt'
procedure_titles.to_csv(output_file_path, header=False, index=False)

print(f"Extracted procedure titles have been saved to {output_file_path}")
