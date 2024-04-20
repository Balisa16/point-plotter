import math
import numpy as np

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
    def nearest_distance(point_a, point_b, point_c)->float:
        a = np.array(point_a)
        b = np.array(point_b)
        c = np.array(point_c)
        
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
        
        return distance