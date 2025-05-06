
import pandas as pd

# Load your Excel file
file_path = 'D:\jd.xlsx'
sheet_data = pd.read_excel(file_path, sheet_name="jd")

# Define the skills keywords to search for
skills_keywords = [
    "Python", "R", "SQL", "Java", "C++", "MATLAB", "Excel", "Pandas", "NumPy", "SAS", "SPSS",
    "Tableau", "Power BI", "Matplotlib", "Seaborn", "D3.js", "Machine Learning", "Deep Learning",
    "TensorFlow", "Keras", "PyTorch", "Scikit-learn", "MySQL", "PostgreSQL", "Oracle", "MongoDB",
    "Hadoop", "Hive", "Spark", "Statistics", "Probability", "Algebra", "Calculus", "Statistical Analysis",
    "BigQuery", "AWS", "Azure", "Google Cloud Platform", "Git", "Docker", "Kubernetes", "APIs", "ETL",
    "Data Wrangling", "Communication", "Collaboration", "Problem-solving", "Critical Thinking",
    "Attention to Detail"
]

# Convert keywords to lowercase
skills_keywords = [skill.lower() for skill in skills_keywords]

# Function to extract keywords
def extract_skills(text, keywords):
    words = text.lower().split()
    found_skills = [word for word in keywords if word in words]
    return list(set(found_skills))

# Apply the extraction
sheet_data['Extracted Skills'] = sheet_data['Job Description'].apply(lambda x: extract_skills(str(x), skills_keywords))

# Display the results
print(sheet_data[['Job Title', 'Extracted Skills']])




 
