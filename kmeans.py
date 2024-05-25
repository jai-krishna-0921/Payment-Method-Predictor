import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load your data
data = pd.read_excel('data_with_updated_values.xlsx')

# Specify the number of clusters you want
num_clusters = 5

# Select the features you want to use for clustering
X = data[['average amount spent', 'what time they purchase']]

# Create a KMeans model
kmeans = KMeans(n_clusters=num_clusters, random_state=0)

# Fit the model to your data
kmeans.fit(X)

# Add cluster labels to your data
data['cluster'] = kmeans.labels_

# Visualize the clusters
plt.scatter(data['average amount spent'], data['how much time they spend'], c=data['cluster'], cmap='viridis')
plt.xlabel('Average Amount Spent')
plt.ylabel('How Much Time They Spend')
plt.title('K-Means Clustering')
plt.show()
