import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel(r'C:\Users\jai krishna\Desktop\Documents\college\ds lab\IDSE Project\preprocessed_data.xlsx')

# Selecting the coloumns
item_columns = [
    'Carbonated Drinks', 'Chicken Puff', 'Chicken Roll', 'Cosmetic items',
    'Electronics (items like headphones', 'Flavored Bun', 'Fruit Drink', 'Ice cream', 'Milkshake',
    'Packeted Chips', 'Printout and Xerox',
    'Stationary Items', 'Veg Roll',
]

# Count frequency
item_counts = data[item_columns].sum()

# pie chart
plt.figure(figsize=(10, 10))
plt.pie(item_counts, labels=item_counts.index, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Percentage of Items Purchased')

#bar graph
plt.figure(figsize=(10, 6))
item_counts.plot(kind='bar')
plt.title('Frequencies of Purchased Items')
plt.xlabel('Purchased Items')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.tight_layout()

# Displaying
plt.show()