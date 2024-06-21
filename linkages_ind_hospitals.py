import pandas as pd
import json
import ast # For ast.literal_eval() function


# Read the CSV file
file_path = 'individual_hospital.csv'
df = pd.read_csv(file_path)

# Extract the 'URL' column
hospital_urls = df['URL']

# Total Columns
columns:int = len(hospital_urls)

# Extract the 'Hospital Name' column
hospital_names = df['Name']

# Extract the 'Hospital City' column
hospital_cities = df['City']

# Extract the 'Hospital Country' column
hospital_countries = df['Country']

# Extract the 'Hospital Bids' column
hospital_beds = df['Beds']

# Extract the 'Established In' column
hospital_established = df['Established In']

# Extract the 'Specialitye' column
hospital_speciality = df['Speciality']

# Extract the 'Header Image 01' column
hospital_images01 = df['Header Image 01']

# Extract the 'Header Image 02' column
hospital_images02 = df['Header Image 02']   

# Extract the 'Patient Experience' column and convert string representations of lists to actual lists
hospital_patient_experience = df['Patient Experience'].apply(ast.literal_eval)

# Extract the 'Medical Departments' column and convert string representations of lists to actual lists
hospital_medical_departments = df['Medical Departments'].apply(ast.literal_eval)

# Extract the 'Hospital Address' column and convert string representations of lists to actual lists
hospital_address = df['Hospital Address'].apply(ast.literal_eval)

# Extract the 'Team And Speciality' column 
hospital_team_speciality = df['Team And Speciality']

# Extract the 'Top Doctors' column and convert string representations of lists to actual lists
hospital_top_doctors = df['Top Doctors'].apply(ast.literal_eval)

# Extract the 'Infrastructure' column and convert string representations of lists to actual lists
hospital_infrastructure = df['Infrastructure'].apply(ast.literal_eval)


# Extract the 'Location' column 
hospital_location = df['Location']


# Extract the 'Facilities' column and convert string representations of lists to actual lists
hospital_facilities = df['Facilities'].apply(ast.literal_eval)

json_data = []

def get_reviews(reviews):
    reviews_list = []
    for review in reviews:
        reviews_list.append(review)
    return reviews_list

def get_medical_departments(medical_departments):
    medical_departments_list = []
    for department in medical_departments:
        medical_departments_list.append(department)
    return medical_departments_list

def get_address(address):
    address_list = []
    for addr in address:
        if addr == "" or addr == " ":
            continue
        address_list.append(addr)
    return address_list

def get_top_doctors(top_doctors):
    top_doctors_list = []
    for doctor in top_doctors:
        top_doctors_list.append(doctor)
    return top_doctors_list

def get_infrastructure(infrastructure):
    infrastructure_list = []
    for infra in infrastructure:
        if infra == "" or infra == " ":
            continue
        infrastructure_list.append(infra)
    return infrastructure_list

def get_facilities(facilities):
    facilities_list = []
    for facility in facilities:
        nstFac = []
        for f in facility:
            if f == "" or f == " ":
                continue
            nstFac.append(f)
        facilities_list.append(nstFac)
    return facilities_list
##############################################
for i in range(columns):
    # Check if the data is missing or NaN
    if pd.isnull(hospital_speciality[i]):
        hospital_speciality[i] = 'N/A'
    if pd.isnull(hospital_images01[i]):
        hospital_images01[i] = 'N/A'
    if pd.isnull(hospital_images02[i]):
        hospital_images02[i] = 'N/A'
        
    if pd.isnull(hospital_location[i]):
        hospital_location[i] = 'N/A'
        
    ##############################################
    # Append the data to the JSON file
    ##############################################
    json_data.append({
        'URL': hospital_urls[i],
        'Hospital Name': hospital_names[i],
        'Hospital City': hospital_cities[i],
        'Hospital Country': hospital_countries[i],
        'Hospital Beds': hospital_beds[i],
        'Established In': hospital_established[i],
        'Speciality': hospital_speciality[i] ,
        'Header Image 01': hospital_images01[i],
        'Header Image 02': hospital_images02[i],
        'Reviews': get_reviews(hospital_patient_experience[i]),
        'Medical Departments': get_medical_departments(hospital_medical_departments[i]),
        'Hospital Address': get_address(hospital_address[i]),
        'Team And Speciality': hospital_team_speciality[i],
        'Top Doctors': get_top_doctors(hospital_top_doctors[i]),
        'Infrastructure': get_infrastructure(hospital_infrastructure[i]),
        'Location': hospital_location[i],
        'Facilities': get_facilities(hospital_facilities[i]),
    })
    

# Create a JSON file
with open('individual_hospital.json', 'w') as f:
    json.dump(json_data, f, indent=4)