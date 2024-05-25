import pandas as pd
from sklearn.cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt

# Specify the path to the preprocessed data file
preprocessed_file_path = 'preprocessed_data.xlsx'

# Load the preprocessed data
df = pd.read_excel(preprocessed_file_path)

# Select the features for clustering
features = df[['average amount spent', 'gender', 'year of study', 'what time they purchase', 'how they make payments']]

# Determine the number of clusters (you can adjust this value)
num_clusters = 5

# Apply K-Means clustering
kmeans = KMeans(n_clusters=num_clusters, random_state=0)
kmeans.fit(features)

# Add cluster labels to the DataFrame
df['cluster'] = kmeans.labels_

# Create a pairplot for different pairs of features with a larger height
g = sns.pairplot(df, hue='cluster', palette='Dark2', height=4)  # Use the 'height' parameter

plt.suptitle('K-Means Clustering', y=1.02)  # Set a title
plt.show()

# You can save the DataFrame with cluster labels to a new file if needed
df.to_excel('clustered_data.xlsx', index=False)
