from sklearn import svm
from sklearn.externals import joblib
import numpy as np

with open("iris_training.csv", 'r') as file:
    header = file.readline()
    data = np.loadtxt(file, delimiter=',', usecols=(0,1,2,3,4))

inputs = data[:,0:2]
labels = data[:,4]

type0 = inputs[labels==0]
type1 = inputs[labels==1]

training_inputs = np.r_[type0, type1]
training_labels = np.r_[np.zeros(len(type0)),np.ones(len(type1))]

clf = svm.LinearSVC()
clf.fit(training_inputs, training_labels)
joblib.dump(clf, 'linear_svm.pkl') 
