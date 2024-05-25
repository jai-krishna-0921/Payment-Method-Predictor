import pandas as pd

# Assuming your dataset is stored in 'data.xlsx'
file_path = r'C:\Users\jai krishna\Desktop\Documents\college\ds lab\IDSE Project\preprocessed_data.xlsx'
df = pd.read_excel(file_path)

# Assuming 'name' is not a relevant variable for correlation analysis
# If needed, you can modify the list of columns accordingly
columns_for_correlation = df.columns.difference(['name'])

# Compute the correlation matrix
correlation_matrix = df[columns_for_correlation].corr()

# Display the correlation matrix
#print(correlation_matrix)

output_file = r'C:\Users\jai krishna\Desktop\Documents\college\ds lab\IDSE Project\correlation_matrix.xlsx'
correlation_matrix.to_excel(output_file, index=False)
