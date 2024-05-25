'''
import pandas as pd
import statsmodels.api as sm

# Load your dataset (with the "average amount spent" column already normalized)
file_path = r'C:\Users\jai krishna\Desktop\Documents\college\ds lab\IDSE Project\data_normalized.xlsx'
data = pd.read_excel(file_path)

# Define the features (independent variables) and the target variable (dependent variable)
X = data[['what time they purchase']]
y = data['average amount spent']

# Add a constant (intercept) to the independent variables
X = sm.add_constant(X)

# Create a linear regression model
model = sm.OLS(y, X)

# Fit the model
results = model.fit()

# Print the summary of the model
print(results.summary())
'''
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Load your dataset (with the "average amount spent" column already normalized)
file_path = r'C:\Users\jai krishna\Desktop\Documents\college\ds lab\IDSE Project\data_normalized.xlsx'
data = pd.read_excel(file_path)

# Define the features (independent variables) and the target variable (dependent variable)
X = data[['what time they purchase']]
y = data['average amount spent']

# Add a constant (intercept) to the independent variables
X = sm.add_constant(X)

# Create a linear regression model
model = sm.OLS(y, X)

# Fit the model
results = model.fit()

# Summary of the model
print(results.summary())

# Residual Plot
plt.figure(figsize=(8, 6))
plt.scatter(results.fittedvalues, results.resid, alpha=0.5)
plt.xlabel("Fitted Values")
plt.ylabel("Residuals")
plt.title("Residual Plot")
plt.show()

# Regression Plot
plt.figure(figsize=(8, 6))
plt.scatter(X['what time they purchase'], y, label="Actual")
plt.plot(X['what time they purchase'], results.fittedvalues, color='red', label="Regression Line")
plt.xlabel("Time of Purchase")
plt.ylabel("Average Amount Spent")
plt.title("Regression Plot")
plt.legend()
plt.show()

# Additional plots and diagnostics can be added as needed
