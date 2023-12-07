import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import quaternion
import math

# Function to create a pyramid
def create_pyramid(x, y, z, qw, qx, qy, qz):
    vertices = np.array([
        [0, 0, 0],  # Apex of the pyramid
        [-.5, .5, 1],  # Base vertex 1
        [.5, .5, 1],  # Base vertex 2
        [.5, -.5, 1], # Base vertex 3
        [-.5, -.5, 1]  # Base vertex 4
    ])

    q = np.quaternion(qw, qx, qy, qz)
    
    rotated_vertices = quaternion.rotate_vectors(q, vertices)

    # Translate the vertices based on the given (x, y, z) translation
    rotated_vertices += np.array([x, y, z])

    # Define triangular faces of the pyramid
    faces = [
        [rotated_vertices[0], rotated_vertices[1], rotated_vertices[2]],
        [rotated_vertices[0], rotated_vertices[2], rotated_vertices[3]],
        [rotated_vertices[0], rotated_vertices[3], rotated_vertices[4]],
        [rotated_vertices[0], rotated_vertices[4], rotated_vertices[1]],
        [rotated_vertices[1], rotated_vertices[2], rotated_vertices[3], rotated_vertices[4]]
    ]

    return Poly3DCollection(faces, edgecolor='k', linewidths=1, alpha=0.5, facecolors='cyan')

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = 0.0
y = 0.0
z = 0.0
qw = 1.0
qx = 0.0
qy = 0.0
qz = 0.0

# Add the pyramid to the plot
ax.add_collection3d(create_pyramid(x, y, z, qw, qx, qy, qz))

# Set axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set aspect ratio to 'equal' for better visualization
ax.set_box_aspect([1, 1, 1])

# Show the plot
plt.show()
