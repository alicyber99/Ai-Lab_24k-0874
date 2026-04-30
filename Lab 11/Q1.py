# importing libraries 
import numpy as nm 
import matplotlib.pyplot as mtp 
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
666
df = pd.read_csv('Mall_Customers.csv')
X = df.drop(columns=['CustomerID']).values

kmeans1 = KMeans(n_clusters=5, init='k-means++', random_state=42)
y1 = kmeans1.fit_predict(X)
age = X[:, 0]
X_rest = X[:, 1:]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_rest)
X_final = nm.column_stack((age, X_scaled))
kmeans2 = KMeans(n_clusters=5, init='k-means++', random_state=42)
y2 = kmeans2.fit_predict(X_final)
mtp.scatter(X[:,1], X[:,2], c=y2)
mtp.title('Customer Clusters (With Scaling)')
mtp.xlabel('Income')
mtp.ylabel('Spending Score')
mtp.show()
