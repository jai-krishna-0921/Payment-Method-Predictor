import pandas as pd
from sklearn.preprocessing import StandardScaler

data = pd.read_excel('data_no_outliers.xlsx')

# Define the column to normalize
column_to_normalize = 'average amount spent'

scaler = StandardScaler()

data[column_to_normalize] = scaler.fit_transform(data[[column_to_normalize]])

# Save the normalized data to a new Excel file
normalized_data_file = 'normalized_data.xlsx'
data.to_excel(normalized_data_file, index=False)
