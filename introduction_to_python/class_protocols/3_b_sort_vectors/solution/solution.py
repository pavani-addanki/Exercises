from math import sqrt
class Vector3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return f"(x = {self.x}, y = {self.y}, z = {self.z})"

    def magnitude(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def __lt__(self, other):
        return self.magnitude() < other.magnitude()

    def __gt__(self, other):
        return self.magnitude() > other.magnitude()
    
    def __eq__(self, other):
        return self.magnitude() == other.magnitude()
    

def sort_vectors(vect_lst):
    n = len(vect_lst)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if vect_lst[j] > vect_lst[j+1] : 
                vect_lst[j], vect_lst[j+1] = vect_lst[j+1], vect_lst[j] 
    return vect_lst