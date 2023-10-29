import numpy as np

data = np.loadtxt("lake-data-raw.csv", float, skiprows=1, delimiter=",")
print(data.shape)