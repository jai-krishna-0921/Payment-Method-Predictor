import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load your dataset
file_path = r'C:\Users\jai krishna\Desktop\Documents\college\ds lab\IDSE Project\normalized_data.xlsx'
data = pd.read_excel(file_path)

# Define the features (purchases) and target variable (how they make payments)
features = ['gender', 'year of study', 'average amount spent']
X = data[features]
y = data['how they make payments']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a Support Vector Machine classifier
clf = SVC()
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)
# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

# Create a dictionary to map purchase items to columns
purchase_item_map = { 
    'gender': '',
    'year of study': 0,
    'average amount spent': 0.0,
}

print("Enter the following details:")

# Gender input
while True:
    gender_input = input('Gender (Male - 1/Female - 0): ').strip().lower()
    if gender_input in ['male', 'female']:
        purchase_item_map['gender'] = 1 if gender_input == 'male' else 0
        break
    else:
        print("Invalid input. Please enter 'Male' or 'Female'.")

# Year of Study input
purchase_item_map['year of study'] = int(input('Year of Study (1/2/3/4): '))

# Average Amount Spent input
purchase_item_map['average amount spent'] = float(input('average amount spent: '))

# Create a DataFrame for the input data
input_data = pd.DataFrame([purchase_item_map])

# Make a prediction for the input data
predicted_payment = clf.predict(input_data)

# Map the predicted payment code back to its actual label
payment_mapping = {
    1: 'Cash',
    2: 'UPI',
}

# Output the predicted payment method
predicted_payment_label = payment_mapping[predicted_payment[0]]
print(f'Predicted payment method: {predicted_payment_label}')