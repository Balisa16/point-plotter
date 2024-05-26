import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from src.view_conv import Conv as vw
from .file import separate_odometry

class Draw:
    def __init__(self, title:str = 'Drone Trajectory', scale = 0.1):
        self.title = title
        self.scale = scale
        self.conv = vw()
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(2, 2, 1, projection='3d')
    
    def append(self, line_name:str, odometry_list:list, color='red', marker='.', draw_camera=False):
        ts, x, y, z , qw, qx, qy, qz = separate_odometry(odometry_list)
        data = list(zip(x, y, z, qw, qx, qy, qz))
        self.ax.plot(x, y, z, marker=marker, color=color, label=line_name)
        if draw_camera:
            for i in data:
                self.ax.add_collection3d(self.conv.create_pyramid(0.8, i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
    
    def get_fig(self):
        return self.fig

    def draw(self):
        # plt.axis('equal')
        # plt.subplots_adjust(left=0, bottom=0, right=1, top=1)
        mng = plt.get_current_fig_manager()
        mng.resize(*mng.window.maxsize())
        mng.set_window_title(self.title)

        # self.ax.set_box_aspect([1,1,1])

        self.ax.set_xlabel('x axis (m)')
        self.ax.set_ylabel('y axis (m)')
        self.ax.set_zlabel('z axis (m)')

        self.ax.legend()

        plt.show()