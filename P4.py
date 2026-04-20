# -----------------------------------
# Practical -4
# Clustering: K-Means & DBSCAN
# -----------------------------------

# ===============================
# PART A: K-Means Clustering
# ===============================

# Step 1: Import Libraries
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs


# Step 2: Create Dataset
X, y = make_blobs(n_samples=200, centers=3, random_state=42)

df = pd.DataFrame(X, columns=['Feature1', 'Feature2'])
print("Initial Data:\n", df.head())


# Step 3: Apply K-Means
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)


# Step 4: Get Cluster Labels
df['KMeans_Cluster'] = kmeans.labels_
print("\nK-Means Result:\n", df.head())


# Step 5: Cluster Centers
print("\nCluster Centers:")
print(kmeans.cluster_centers_)


# ===============================
# PART B: DBSCAN Clustering
# ===============================

# Step 1: Import Libraries
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler


# Step 2: Standardize Data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# Step 3: Apply DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=5)
dbscan.fit(X_scaled)


# Step 4: Get Cluster Labels
df['DBSCAN_Cluster'] = dbscan.labels_
print("\nDBSCAN Result:\n", df.head())


# Step 5: Identify Noise Points
noise_points = df[df['DBSCAN_Cluster'] == -1]
print("\nNumber of Noise Points:", len(noise_points))