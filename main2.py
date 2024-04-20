import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

filename = 'docs/track.csv'
data = []
header = "None"
try:
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        for row in csv_reader:
            data.append(row)
except FileNotFoundError:
    print(f"File not found: {filename}")
except Exception as e:
    print(f"An error occurred: {e}")

label = []
sim_x = []
sim_y = []
sim_z = []
target_x = []
target_y = []
target_z = []
for row in data:
    label.append(row[0])
    sim_x.append(float(row[3]))
    sim_y.append(float(row[4]))
    sim_z.append(float(row[5]))
    target_x.append(float(row[10]))
    target_y.append(float(row[11]))
    target_z.append(float(row[12]))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(sim_x, sim_y, sim_z, marker='o')
ax.plot(target_x, target_y, target_z, marker='o')
mng = plt.get_current_fig_manager()
mng.resize(*mng.window.maxsize())
plt.axis('equal')

ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

plt.show()