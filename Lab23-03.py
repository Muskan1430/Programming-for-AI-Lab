import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans, DBSCAN
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
import numpy as np

#Load dataset
iris =load_iris()
X= iris.data[:, :2] #Take only first 2 features for visualization

#Data Preprocesing
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# K-MEANS CLUSTERING
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans_labels = kmeans.fit_predict(X_scaled)
print("Labels",kmeans_labels)

#Plot K_Means
plt.figure()
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=kmeans_labels, cmap='viridis')
plt.title("K-Means Clustering (Iris Dataset)")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()

#Plot Decision
dbscan = DBSCAN(eps=0.5, min_samples=5)
dbscan_labels = dbscan.fit_predict(X_scaled)
print("DBSCAN Labels:\n",dbscan_labels)
plt.figure()
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=dbscan_labels, cmap='viridis')
plt.title("DBSCAN Clustering (Iris Dataset)")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()

#Choose min-samples
min_samples = 4
#Compute nearest neighbors
neighbors = NearestNeighbors(n_neighbors=min_samples)
neighbors_fit = neighbors.fit(X_scaled)
#Get distances
distances, indices = neighbors_fit.kneighbors(X_scaled)
print("Distances:\n", distances)
print("Indices:\n", indices)
#Sort distances
distanecs = np.sort(distances[:, -1])
#Plot
plt.plot(distances)
plt.title("K-Distance Graph")