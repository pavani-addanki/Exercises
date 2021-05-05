from math import sqrt
class Vector3D:
        
    def __init__(self,x = 0,y = 0,z = 0):
        self.x = x
        self.y = y
        self.z = z
        
    def __abs__(self):
        return sqrt(self.x*self.x + self.y*self.y + self.z*self.z)


