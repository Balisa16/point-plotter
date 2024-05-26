import csv
from src.distance import Nearest, Pos
import numpy as np
from .datatypes import *
import math
import pandas as pd

def separate_odometry(data:list):
    ts:list = []
    x:list = []
    y:list = []
    z:list = []
    qw:list = []
    qx:list = []
    qy:list = []
    qz:list = []
    for item in data:
        ts.append(item.timestamp)
        x.append(item.position.x)
        y.append(item.position.y)
        z.append(item.position.z)
        qw.append(item.orientation.qw)
        qx.append(item.orientation.qx)
        qy.append(item.orientation.qy)
        qz.append(item.orientation.qz)
    return ts, x, y, z, qw, qx, qy, qz

class CSVreader:
    def __init__(self, filename):
        self.filename = filename
        self.data = []
        self.header = "None"
        self.ts:list = []
        try:
            with open(self.filename, 'r') as file:
                csv_reader = csv.reader(file)
                self.header = next(csv_reader)
                for row in csv_reader:
                    self.ts.append(float(row[2]))
                    self.data.append(row)
        except FileNotFoundError:
            print(f"File not found: {filename}")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    def get_ts(self)->list:
        return self.ts

    def get_data(self):
        return self.data
    
    def get_header(self):
        return self.header

    def get_item(self):
        odometry_list:list = []

        prev_pos = Position(0.0, 0.0, 0.0)
        next_pos = Position(0.0, 0.0, 0.0)
        temp_pos = Position(0.0, 0.0, 0.0)
        temp_odometry = Odometry(0.0, Position(0.0, 0.0, 0.0), Orientation(0.0, 0.0, 0.0, 0.0))
        
        errors:list = []
        errors2:list = []
        
        x_error:list = []
        y_error:list = []
        z_error:list = []

        ground_truth_list:list = []
        pos_list:list = []
        _cnt = 0
        max_dist = 0.0
        min_dist = float('inf')
        traj_length = 0.0
        
        for row in self.data:
            current_pos = Position(float(row[3]), float(row[4]), float(row[5]))
            current_orient = Orientation(float(row[6]), float(row[7]), float(row[8]), float(row[9]))
            current_odometry = Odometry(row[0], current_pos, current_orient)
            odometry_list.append(current_odometry)
            temp_pos = Position(float(row[10]), float(row[11]), float(row[12]))
            
            if temp_pos != next_pos :
                pos_list.append([_cnt, temp_pos])
                traj_length += math.sqrt((temp_pos.x - next_pos.x)**2 + (temp_pos.y - next_pos.y)**2 + (temp_pos.z - next_pos.z)**2)
                prev_pos = next_pos
                next_pos = temp_pos
                ground_truth_list.append(Odometry(row[0], Position(float(row[10]), float(row[11]), float(row[12])), Orientation(float(row[6]), float(row[7]), float(row[8]), float(row[9]))))
            
            dist, x_err, y_err, z_err = Nearest.nearest_distance(prev_pos, next_pos, current_pos)
            
            max_dist = max(max_dist, dist)
            min_dist = min(min_dist, dist)

            x_error.append(x_err)
            y_error.append(y_err)
            z_error.append(z_err)

            errors.append(dist)
            errors2.append(dist**2)
            _cnt += 1
            # print("{:.4f}".format(dist))
        print("MAE : ", "{:.4f}".format(np.mean(errors)))
        print("MSE : ", "{:.4f}".format(np.mean(errors2)))
        print("Max. Error : ", "{:.4f}".format(max_dist))
        print("Min. Error : ", "{:.4f}".format(min_dist))
        print("Trajectory Length : ", "{:.4f}".format(traj_length))
        
        last_data = self.data[len(self.data) - 1]
        ground_truth_list.append(Odometry(row[0], 
                                          Position(float(last_data[10]), float(last_data[11]), float(last_data[12])), 
                                          Orientation(float(last_data[6]), float(last_data[7]), float(last_data[8]), float(last_data[9]))))
        
        return odometry_list, ground_truth_list, x_error, y_error, z_error, errors, pos_list
    
    def get_odometry(self):
        ret_val:list = []
        for row in self.data:
            ret_val.append(Odometry(
                            row[3],
                            Position(
                                float(row[3]),
                                float(row[4]),
                                float(row[5])),
                            Orientation(
                                float(row[6]),
                                float(row[7]),
                                float(row[8]),
                                float(row[9]))))
        return ret_val
