import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

with open("boston.csv", 'r') as file:
    line = file.readline()
    data = np.loadtxt(file, delimiter=',', usecols=(10,13))

inputs = data[:,0]
inputs = inputs[:,np.newaxis] # convert [*,*,*,..] -> [[*],[*],[*],...]

outputs = data[:,1]

regr = linear_model.LinearRegression()
regr.fit(inputs, outputs)

print('Coefficients: \n', regr.coef_)

# plot
x_min = np.min(inputs)
x_max = np.max(inputs)
plot_x = np.arange(x_min,x_max,0.1)
plot_x = plot_x[:,np.newaxis] # convert [*,*,*,..] -> [[*],[*],[*],...]
plt.scatter(inputs[:,0], outputs,  color='black')
plt.plot(plot_x[:,0], regr.predict(plot_x), color='red')
plt.show()
