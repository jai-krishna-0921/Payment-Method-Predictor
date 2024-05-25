import pandas as pd
import matplotlib.pyplot as plt

file_path = r'C:\Users\jai krishna\Desktop\Documents\college\ds lab\IDSE Project\preprocessed_data.xlsx'
data = pd.read_excel(file_path)

column_to_analyze = 'what time they purchase'

# Create a box plot to visualize the distribution and identify outliers
plt.figure(figsize=(8, 6))
plt.boxplot(data[column_to_analyze], vert=False)
plt.title("Box Plot of Average Amount Spent")
plt.show()

# Calculate the interquartile range
Q1 = data[column_to_analyze].quantile(0.25)
Q3 = data[column_to_analyze].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identify and save the outliers
outliers = data[(data[column_to_analyze] < lower_bound) | (data[column_to_analyze] > upper_bound)]

data_no_outliers = data[(data[column_to_analyze] >= lower_bound) & (data[column_to_analyze] <= upper_bound)]

print("Outliers (removed rows):")
print(outliers)

print("Previous Data Shape:", data.shape)
print("Data Shape After Removing Outliers:", data_no_outliers.shape)

output_file = r'C:\Users\jai krishna\Desktop\Documents\college\ds lab\IDSE Project\data_no_outliers.xlsx'
data_no_outliers.to_excel(output_file, index=False)
