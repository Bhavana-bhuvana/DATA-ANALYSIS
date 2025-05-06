import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load the "jd1" sheet
file_path ="D:\da\python.xlsx"
data = pd.ExcelFile(file_path)
jd1_data = data.parse('jd1')

# Features: Select binary skill columns
features = ['python', 'sql', 'artificial intelligence', 'google cloud platform',
            'deep learning', 'statistics', 'machine learning', 'power bi',
            'tableau', 'etl']
X = jd1_data[features]

# Target: Use the simplified job title as the classification label
y = jd1_data['Job_Title_Simplified']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train logistic regression model
model = LogisticRegression(max_iter=1000, multi_class='multinomial', solver='lbfgs')
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.4f}')
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Display confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
