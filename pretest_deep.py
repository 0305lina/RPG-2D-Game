import numpy as np
from sklearn.cluster import KMeans

# Create a mock dataset (replace with actual data)
data = np.random.rand(9, 3)  # 9 questions, 3 sections

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

num_clusters = 3  # Number of sections
kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(scaled_data)

cluster_labels = kmeans.labels_

cluster_avg_scores = []
for i in range(num_clusters):
    cluster_indices = np.where(cluster_labels == i)
    avg_score = np.mean(data[cluster_indices], axis=0)
    cluster_avg_scores.append(avg_score)

weakest_section = np.argmin(np.mean(cluster_avg_scores, axis=1))

print(f"The weakest section is Section {weakest_section + 1}.")
print("Please focus on improving your performance in this section.")
