import pandas as pd
import re

# Read the CSV file
file_path = 'individual_hospital.csv'
df = pd.read_csv(file_path)

# Extract the 'Medical Departments' column
medical_departments = df['Medical Departments']

# Split the department names and expand into a DataFrame
individual_departments = medical_departments.apply(lambda x: x.strip("[]").replace("'", "").split(', '))

# Flatten the list of lists into a single list
flattened_departments = [dept for sublist in individual_departments for dept in sublist]

# Remove any empty strings and surrounding spaces
flattened_departments = [dept.strip() for dept in flattened_departments if dept.strip()]

# Remove (x) where x is any integer and remove the last part of each department name that includes (x)
processed_departments = []
for dept in flattened_departments:
    processed_dept = re.sub(r'\(\d+\)', '', dept)  # Remove (x)
    processed_dept = re.sub(r'\s*\([^)]*\)$', '', processed_dept)  # Remove the last part with (x)
    processed_departments.append(processed_dept)

# Remove duplicates while preserving the order
unique_departments = list(dict.fromkeys(processed_departments))

# Save to a .txt file
output_file_path = 'individual_medical_departments.txt'
with open(output_file_path, 'w') as file:
    for dept in unique_departments:
        file.write(dept + '\n')

print(f"Individual medical department names (without duplicates and processed) have been saved to {output_file_path}")
