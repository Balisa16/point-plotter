import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import quaternion
from scipy.spatial.transform import Rotation
import math

# Function to create a pyramid

class Conv:
    def __init__(self):
        pass

    def quaternion_to_euler(self, quaternion):
        # Create a Rotation object from the quaternion
        rotation = Rotation.from_quat(quaternion)
        
        # Get the Euler angles in degrees
        euler_angles = rotation.as_euler('zyx', degrees=True)
        
        return euler_angles

    def euler_to_quaternion(self, roll, pitch, yaw):
        # Create a Rotation object from Euler angles
        rotation = Rotation.from_euler('zyx', [yaw, pitch, roll], degrees=True)
        
        # Get the quaternion representation
        quaternion = rotation.as_quat()
        
        return quaternion
    def create_pyramid(self, scale, x, y, z, qw, qx, qy, qz):
        vertices = np.array([
            [0, 0, 0],  # Apex of the pyramid
            [-.5*scale, .5*scale, 1*scale],  # Base vertex 1
            [.5*scale, .5*scale, 1*scale],  # Base vertex 2
            [.5*scale, -.5*scale, 1*scale], # Base vertex 3
            [-.5*scale, -.5*scale, 1*scale]  # Base vertex 4
        ])

        self.qw = float(qw)
        self.qx = float(qx)
        self.qy = float(qy)
        self.qz = float(qz)

        cv = Conv()

        view_quat = cv.quaternion_to_euler(np.array([self.qz, self.qy, self.qx, self.qw]))

        print(view_quat)

        if view_quat[2] < 270:
            view_quat[2] += 90
        else:
            view_quat[2] = 270 - view_quat[2]
        
        view_quat[1] -= 90
 
        quat_result = cv.euler_to_quaternion(view_quat[0], view_quat[2], view_quat[1])

        q = np.quaternion(quat_result[0], quat_result[1], quat_result[2], quat_result[3])
        
        rotated_vertices = quaternion.rotate_vectors(q, vertices)

        rotated_vertices += np.array([float(x), float(y), float(z)])

        faces = [
            [rotated_vertices[0], rotated_vertices[1], rotated_vertices[2]],
            [rotated_vertices[0], rotated_vertices[2], rotated_vertices[3]],
            [rotated_vertices[0], rotated_vertices[3], rotated_vertices[4]],
            [rotated_vertices[0], rotated_vertices[4], rotated_vertices[1]],
            [rotated_vertices[1], rotated_vertices[2], rotated_vertices[3], 
            rotated_vertices[4]]
        ]

        return Poly3DCollection(faces, edgecolor='k', linewidths=1, alpha=0.5, facecolors='cyan')

# # Create a 3D plot
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# scale = 0.1
# x = 0.2
# y = 0.0
# z = 0.0
# qw = 1.0
# qx = 0.0
# qy = 0.0
# qz = 0.0

# # Add the pyramid to the plot
# cv = Conv()
# cnt = 0
# for i in range(36):
#     quat_result = cv.euler_to_quaternion(i*10, 0, 0)
#     print(quat_result)
#     ax.add_collection3d(cv.create_pyramid(scale, cnt, y, z, quat_result[3]*10, quat_result[0]*10, qy, qz))
#     cnt += 1

# # Set axis labels
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')

# # Set aspect ratio to 'equal' for better visualization
# ax.set_box_aspect([1, 1, 1])
# plt.xlim([0,36])

# # Show the plot
# plt.show()
