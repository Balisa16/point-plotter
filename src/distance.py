import math

class Pos:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

class Nearest:
    @staticmethod
    def nearest_distance(pos1:Pos, pos2:Pos, posc:Pos)->float:
        dx = pos2.x - pos1.x
        dy = pos2.y - pos1.y
        dz = pos2.z - pos1.z

        t = ((posc.x - pos1.x) * dx + (posc.y - pos1.y) * dy + (posc.z - pos1.z) * dz) / (dx * dx + dy * dy + dz * dz)

        x_near = pos1.x + t * dx
        y_near = pos1.y + t * dy
        z_near = pos1.z + t * dz

        dist_near = Nearest.distance(posc, Pos(x_near, y_near, z_near))
        return dist_near

    @staticmethod
    def distance(pos1:Pos, pos2:Pos)->float:
        return math.sqrt((pos2.x - pos1.x) ** 2 + (pos2.y - pos1.y) ** 2 + (pos2.z - pos1.z) ** 2)
