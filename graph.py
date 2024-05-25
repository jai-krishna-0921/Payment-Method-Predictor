import pandas as pd
import matplotlib.pyplot as plt

# Specify the path to your preprocessed data file
preprocessed_file_path = 'data_with_updated_values.xlsx'

# Load the preprocessed data
df = pd.read_excel(preprocessed_file_path)

# Extract the "average amount spent" and "what time they purchase" columns
average_amount_spent = df['average amount spent']
hom_much_time_they_spend = df['how much time they spend']

# Create a scatter plot
plt.scatter(average_amount_spent, hom_much_time_they_spend, alpha=0.5)
plt.ylabel('hom_much_time_they_spend')
plt.xlabel('Average Amount Spent')
plt.title('Scatter Plot: Time They Purchase vs. Average Amount Spent')

plt.show()
