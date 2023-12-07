import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class Draw:
    def __init__(self, ts, x, y, z):
        self.ts = ts
        self.x = x
        self.y = y
        self.z = z
        self.data = list(zip(self.x, self.y, self.z))

    def draw(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # # x, y, z = zip(self.data)
        ax.plot(self.x, self.y, self.z, marker='o')
        # plt.axis('equal')
        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed') 

        ax.set_xlabel('X Axis')
        ax.set_ylabel('Y Axis')
        ax.set_zlabel('Z Axis')

        plt.show()