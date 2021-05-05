from math import sqrt
class Vector3D:
        
    def __init__(self,x = 0,y = 0,z = 0):
        self.x = x
        self.y = y
        self.z = z
        
    def __lt__(self,other):
        if magnt(self) < magnt(other):
            return True
        else:
            return False
    
    def __gt__(self,other):
        if magnt(self) > magnt(other):
            return True
        else:
            return False

def magnt(vect):
    return sqrt(vect.x*vect.x + vect.y*vect.y + vect.z*vect.z)
