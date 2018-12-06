from sklearn import cluster
import numpy as np

with open("iris.csv", 'r') as file:
    header = file.readline()
    data = np.loadtxt(file, delimiter=',', usecols=(0,1,2,3,4))

inputs = data[:,0:4]
labels = data[:,4]

K = 3
model = cluster.KMeans(n_clusters=K).fit(inputs)
results = model.predict(inputs)

print("Original  : {0}".format(labels.astype(np.int64)))
print("Clustering: {0}".format(results))
