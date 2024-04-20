import csv
from src.distance import Nearest, Pos
import numpy as np

class PosOrient:
    def __init__(self, ts,
                 x:float, y:float, z:float, 
                 qw:float, qx:float, qy:float, qz:float):
        self.ts = ts
        self.x = x
        self.y = y
        self.z = z
        self.qw = qw
        self.qx = qx
        self.qy = qy
        self.qz = qz

class CSVreader:
    def __init__(self, filename):
        self.filename = filename
        self.data = []
        self.header = "None"
        try:
            with open(self.filename, 'r') as file:
                csv_reader = csv.reader(file)
                self.header = next(csv_reader)
                for row in csv_reader:
                    self.data.append(row)
        except FileNotFoundError:
            print(f"File not found: {filename}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_data(self):
        return self.data
    
    def get_header(self):
        return self.header

    def get_item(self):
        ts = []
        x = []
        y = []
        z = []
        qw = []
        qx = []
        qy = []
        qz = []
        prev_pos = (0.0, 0.0, 0.0)
        next_pos = (0.0, 0.0, 0.0)
        temp_pos = (0.0, 0.0, 0.0)
        errors:list = []
        for row in self.data:
            ts.append(row[0])
            current_pos = (float(row[3]), float(row[4]), float(row[5]))
            x.append(float(row[3]))
            y.append(float(row[4]))
            z.append(float(row[5]))
            qw.append(row[6])
            qx.append(row[7])
            qy.append(row[8])
            qz.append(row[9])
            temp_pos = (float(row[10]), float(row[11]), float(row[12]))
            if temp_pos != next_pos :
                prev_pos = next_pos
                next_pos = temp_pos
            dist:float = Nearest.nearest_distance(prev_pos, next_pos, current_pos)
            errors.append(dist)
            print(row[0], " : ", "{:.4f}".format(dist))
        print(f"MAE : {np.mean(errors)}")
        return ts, x, y, z, qw, qx, qy, qz
    
    def get_pos_orient(self):
        ret_val = []
        for row in self.data:
            ret_val.append(PosOrient(
                            float(row[3]),
                            float(row[4]),
                            float(row[5]),
                            float(row[6]),
                            float(row[7]),
                            float(row[8]),
                            float(row[9]),
                            float(row[10])))
        return ret_val
