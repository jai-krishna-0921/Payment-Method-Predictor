import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, accuracy_score

# Load your preprocessed and outlier-free data
data = pd.read_excel('normalized_data.xlsx')

# Define the features (X) and target variable (y)
features = ['average amount spent', 'year of study', 'how much time they spend',
            'Carbonated Drinks', 'Chicken Puff', 'Chicken Roll', 'Cosmetic items',
            'Electronics (items like headphones', 'Flavored Bun', 'Fruit Drink',
            'Ice cream', 'Milkshake', 'Packeted Chips', 'Printout and Xerox',
            'Stationary Items', 'Veg Roll']


# Ensure that all feature columns are present in the dataset
missing_columns = [col for col in features if col not in data.columns]
if missing_columns:
    raise ValueError(f"Missing columns in the dataset: {missing_columns}")

X = data[features]
y = data['how they make payments']  # Target variable is 'how they make payments'

# Normalize the continuous features (e.g., 'average amount spent')
scaler = StandardScaler()
X[['average amount spent', 'how much time they spend']] = scaler.fit_transform(X[['average amount spent', 'how much time they spend']])

# Split the data into a training set and a testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create an SVM model
model = SVC()

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
classification_report_str = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print('Classification Report:\n', classification_report_str)

# You can use this model to make predictions for new data.
