import math
import numpy as np
from src.datatypes import Position

class Pos:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z
    
    def __eq__(self, other):
        if isinstance(other, Pos):
            return self.x == other.x and self.y == other.y and self.z == other.z
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

class Nearest:
    @staticmethod
    def nearest_distance(point_a:Position, point_b:Position, point_c:Position)->float:
        a = point_a.to_numpy()
        b = point_b.to_numpy()
        c = point_c.to_numpy()
        
        # Vektor AC dan AB
        ac = c - a
        ab = b - a
        
        # Proyeksi vektor AC ke vektor AB
        projection = np.dot(ac, ab) / np.dot(ab, ab) * ab
        
        # Vektor normal ke vektor AB
        normal_vector = ac - projection
        
        # Panjang vektor normal
        normal_length = np.linalg.norm(normal_vector)
        
        # Jarak minimum
        distance = normal_length
        
        error_x = c[0] - (a[0] + projection[0])
        error_y = c[1] - (a[1] + projection[1])
        error_z = c[2] - (a[2] + projection[2])
        
        return distance, error_x, error_y, error_z
