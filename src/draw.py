import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from src.viewConv import Conv as vw

class Draw:
    def __init__(self, ts, x, y, z, qw, qx, qy, qz, scale = 0.1):
        self.ts = ts
        self.x = x
        self.y = y
        self.z = z
        self.qw = qw
        self.qx = qx
        self.qy = qy
        self.qz = qz
        self.scale = scale
        self.data = list(zip(self.x, self.y, self.z, self.qw, self.qx, self.qy, self.qz))
        self.conv = vw()

    def draw(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # # x, y, z = zip(self.data)
        ax.plot(self.x, self.y, self.z, marker='o')
        for i in self.data:
            ax.add_collection3d(self.conv.create_pyramid(0.8, i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
        plt.axis('equal')
        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed') 

        ax.set_xlabel('X Axis')
        ax.set_ylabel('Y Axis')
        ax.set_zlabel('Z Axis')

        plt.show()