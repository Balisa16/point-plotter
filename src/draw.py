import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def generate_line_points(start, end, num_points):
    x_vals = np.linspace(start[0], end[0], num_points)
    y_vals = np.linspace(start[1], end[1], num_points)
    z_vals = np.linspace(start[2], end[2], num_points)
    return list(zip(x_vals, y_vals, z_vals))

def draw_3d_line(points):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x, y, z = zip(*points)
    ax.plot(x, y, z, marker='o')

    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')

    plt.show()

# Example: Generate 100 points along a line
start_point = (1, 2, 3)
end_point = (10, 12, 15)
num_points = 100
line_points = generate_line_points(start_point, end_point, num_points)
draw_3d_line(line_points)