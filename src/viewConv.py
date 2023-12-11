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

        rotation = Rotation.from_quat(quaternion)
        
        euler_angles = rotation.as_euler('zyx', degrees=True)
        
        return euler_angles

    def euler_to_quaternion(self, roll, pitch, yaw):
        
        rotation = Rotation.from_euler('zyx', [yaw, pitch, roll], degrees=True)
        
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