import numpy as nm 
import pandas as pd
import matplotlib.pyplot as mtp
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = {
 'student_id': [1,2,3,4,5,6,7,8,9,10],
 'GPA': [3.5,2.8,3.9,2.5,3.2,3.7,2.2,3.8,2.9,3.0],
 'study_hours': [15,8,20,5,12,18,6,19,9,10],
 'attendance_rate': [90,70,95,60,85,92,65,96,75,80]
}

df = pd.DataFrame(data)
X = df[['GPA','study_hours','attendance_rate']].values

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

wcss = []

for i in range(2,7):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

mtp.plot(range(2,7), wcss)
mtp.title('Elbow Method')
mtp.xlabel('Number of clusters')
mtp.ylabel('WCSS')
mtp.show()

kmeans = KMeans(n_clusters=3, random_state=42)
y = kmeans.fit_predict(X_scaled)

df['Cluster'] = y

print(df)
mtp.scatter(df['study_hours'], df['GPA'], c=y)
mtp.title('Student Clusters')
mtp.xlabel('Study Hours')
mtp.ylabel('GPA')
mtp.show()
