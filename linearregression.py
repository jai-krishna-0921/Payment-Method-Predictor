import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score,accuracy_score
# Load your dataset (with the "average amount spent" column already normalized)
file_path = r'C:\Users\jai krishna\Desktop\Documents\college\ds lab\IDSE Project\data_no_outliers.xlsx'
data = pd.read_excel(file_path)

# Define the features and target variable
X = data.drop(columns=['how they make payments', 'name'])
y = data['how they make payments']

print(X)

print(y)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict using the test set
y_pred = model.predict(X_test)

print(y_test)
print(y_pred)

# accuracy = accuracy_score(y_test, y_pred)
# Calculate metrics (optional)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Mean Squared Error:", mse)
print("R-squared:", r2)

# Create a scatter plot with the regression line
plt.figure(figsize=(8, 6))
sns.scatterplot(x=X_test['what time they purchase'], y=y_test, label="Actual")
sns.lineplot(x=X_test['what time they purchase'], y=y_pred, color='red', label="Regression Line")
plt.xlabel("Time of Purchase")
plt.ylabel("Average Amount Spent")
plt.title("Linear Regression: Time of Purchase vs. Average Amount Spent")
plt.legend()
plt.show()

# Make predictions for specific times (e.g., 1 for morning, 2 for afternoon, etc.)
times_to_predict = [1, 2, 3, 4]
times_to_predict = pd.DataFrame(times_to_predict, columns=['what time they purchase'])  # Reshape for prediction
predicted_amounts = model.predict(times_to_predict)

for time, amount in zip(times_to_predict['what time they purchase'], predicted_amounts):
    print(f"For time {time}, the predicted average amount spent is: {amount:.2f}")
