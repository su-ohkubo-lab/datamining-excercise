from sklearn.externals import joblib
import numpy as np
import matplotlib.pyplot as plt

with open("iris_training.csv", 'r') as file:
    line = file.readline()
    data = np.loadtxt(file, delimiter=',', usecols=(0,1,2,3,4))

inputs = data[:,0:2] 
labels = data[:,4]

clf = joblib.load('linear_svm.pkl')

mycolors = ['r', 'b']
for i, mycolor in enumerate(mycolors):
    plt.scatter(inputs[labels==i, 0], inputs[labels==i, 1], color=mycolor) 
x_min = inputs[:, 0].min() - 1
x_max = inputs[:, 0].max() + 1
y_min = inputs[:, 1].min() - 1
y_max = inputs[:, 1].max() + 1
grid_interval = 0.02
x_grids, y_grids = np.meshgrid(
    np.arange(x_min, x_max, grid_interval),
    np.arange(y_min, y_max, grid_interval))
z_grids = clf.predict(np.c_[x_grids.ravel(), y_grids.ravel()])
z_grids = z_grids.reshape(x_grids.shape)
plt.contourf(x_grids, y_grids, z_grids, cmap=plt.cm.bone, alpha=0.2)
plt.show()

