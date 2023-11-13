import numpy as np
import matplotlib.pyplot as plt

# Retrieving data from the file
data = np.loadtxt("lake-data-raw.csv", float, skiprows=1, delimiter=",")
x_vals, y_vals, z_vals = data[:, 0], data[:, 1], -data[:, 2]

# Filtered data lists
x_filtered, y_filtered, z_filtered = [], [], [] 

# Sets to make sure unique values
unique_x = set()
unique_y = set()

# Removing values that hold insignificant x and y values
for i in range(len(x_vals)):
    curr_x, curr_y, curr_z = x_vals[i], y_vals[i], z_vals[i]

    # Check if the current x is unique
    if curr_x not in unique_x and curr_z == 0:
        x_filtered.append(x_vals[i])
        y_filtered.append(y_vals[i])
        z_filtered.append(z_vals[i])
    elif curr_z < 0:
        x_filtered.append(x_vals[i])
        y_filtered.append(y_vals[i])
        z_filtered.append(z_vals[i])
    # Check if the current y is unique
    if curr_y not in unique_y and curr_z == 0:
        x_filtered.append(x_vals[i])
        y_filtered.append(y_vals[i])
        z_filtered.append(z_vals[i])
    elif curr_z < 0:
        x_filtered.append(x_vals[i])
        y_filtered.append(y_vals[i])
        z_filtered.append(z_vals[i])

    # Adding current x and y values to sets
    unique_x.add(curr_x)
    unique_y.add(curr_y)

# Maximum x and y to scale 
max_x = max(x_vals)
max_y = max(y_vals)

# Scaling points to be usable in Blender
scale_mult = 10000
x_filtered = [scale_mult*(x - max_x) for x in x_filtered]
y_filtered = [scale_mult*(y - max_y) for y in y_filtered]
x_vals = [scale_mult*(x - max_x) for x in x_vals]
y_vals = [scale_mult*(y - max_y) for y in y_vals]


file = open('lake_data_processed.txt', 'w')
for x in range(len(x_filtered)):
    file.write(str(x_filtered[x]))
    file.write(',')
    file.write(str(y_filtered[x]))
    file.write(',')
    file.write(str(z_filtered[x]))
    file.write('\n')
file.close()
# plt.plot(x_filtered, y_filtered, label="filtered")
plt.plot(x_vals, y_vals, label="unfiltered")
plt.xlabel("X")
plt.ylabel("Y")

plt.title("Unfiltered")
plt.legend()
plt.show()