import numpy as np

class Position:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x:float = x
        self.y:float = y
        self.z:float = z
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, Position):
            return self.x == value.x and self.y == value.y and self.z == value.z
        return False
    
    def __ne__(self, value: object) -> bool:
        return not self.__eq__(value)

    def to_numpy(self):
        return np.array([self.x, self.y, self.z])
    
    def __str__(self) -> str:
        return f'({self.x}, {self.y}, {self.z})'

class Orientation:
    def __init__(self, qw=0.0, qx=0.0, qy=0.0, qz=0.0):
        self.qw:float = qw
        self.qx:float = qx
        self.qy:float = qy
        self.qz:float = qz

class Odometry:
    def __init__(self, ts,
                 pos:Position, 
                 orient:Orientation):
        self.timestamp = ts
        self.position = pos
        self.orientation = orient
