import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# Load your preprocessed and outlier-free data
data = pd.read_excel('data_no_outliers.xlsx')

# Define the features (X) and target variable (y)
features = ['average amount spent', 'year of study',
            'Carbonated Drinks', 'Chicken Puff', 'Chicken Roll',
            'Chocolates', 'Cosmetic items', 'Electronics (items like headphones)',
            'Flavored Bun', 'Fruit Drink', 'Ice cream', 'Milkshake', 'Packeted Chips',
            'Printout and Xerox', 'Sport Equipment( items like Shuttle cork etc)',
            'Stationary Items', 'Veg Roll']
X = data[features]
y = data['what they purchase']

# Split the data into a training set and a testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a logistic regression model
model = LogisticRegression(max_iter=1000)

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
