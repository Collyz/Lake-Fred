import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("lake-data-raw.csv", float, skiprows=1, delimiter=",")
x_vals, y_vals, z_vals = data[:, 0], data[:, 1], data[:, 2]

x_filtered, y_filtered, z_filtered = [], [], []

unique_x = set()
unique_y = set()

for i in range(len(x_vals)):
    curr_x, curr_y = x_vals[i], y_vals[i]

    # Check if the current (x, y, z) pair is unique
    if curr_x not in unique_x:
        x_filtered.append(x_vals[i])
        y_filtered.append(y_vals[i])
        z_filtered.append(z_vals[i])

    if curr_y not in unique_y:
        x_filtered.append(x_vals[i])
        y_filtered.append(y_vals[i])
        z_filtered.append(z_vals[i])

    unique_x.add(curr_x)
    unique_y.add(curr_y)

max_x = max(x_vals)
min_x = min(x_vals)

max_y = max(y_vals)
min_y = min(y_vals)

scale = 10000
x_filtered = [scale*(max_x - x) for x in x_filtered]
y_filtered = [scale*(max_y - y) for y in y_filtered]
x_vals = [scale*(max_x - x) for x in x_vals]
y_vals = [scale*(max_y - y) for y in y_vals]

plt.plot(x_filtered, y_filtered, label="filtered")
plt.plot(x_vals, y_vals, label="unfiltered")
plt.xlabel("X")
plt.ylabel("Y")

plt.title("Filtered vs. Unfiltered")
plt.legend()
plt.show()
