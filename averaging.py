import pandas as pd
import numpy as np

# Load the existing Excel file
data = pd.read_excel('preprocessed_data.xlsx')

# Specify the standard deviation for generating new values around the existing "Average Amount Spent"
std_deviation = 10  # Adjust this value as needed

# Generate new whole number values around the existing "Average Amount Spent" values
data['average amount spent'] = data['average amount spent'].apply(lambda avg_amount: round(np.random.normal(avg_amount, std_deviation)))

# Save the updated data to the Excel file
data.to_excel('data_with_updated_values.xlsx', index=False)