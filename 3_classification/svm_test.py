from sklearn.externals import joblib
import numpy as np

with open("iris_test.csv", 'r') as file:
    line = file.readline()
    data = np.loadtxt(file, delimiter=',', usecols=(0,1,2,3,4))

inputs = data[:,0:2]
labels = data[:,4]

clf = joblib.load('linear_svm.pkl')
results = clf.predict(inputs)

print("Answer : {0}".format(labels))
print("Predict: {0}".format(results))

