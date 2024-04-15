#Excercise 7.1

import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "Vector({}, {}, {})". format(self.x, self.y, self.z)

    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vector(self.y * other.z - self.z * other.y,
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)

    def length(self):
        return math.sqrt(self * self)

    def __hash__(self):
        return hash((self.x, self.y, self.z))


def find_axis(v1, v2):
    if v1 == Vector(0, 0, 0) or v2 == Vector(0, 0, 0):
        raise ValueError("Input vectors are zero vectors.")
    if v1.cross(v2) == Vector(0, 0, 0):
        raise ValueError("Input vectors are parallel.")
        
    cross_product = v1.cross(v2)
    
    length = cross_product.length()
    unit_vector = Vector(cross_product.x / length, cross_product.y / length, cross_product.z / length)

    return unit_vector

v = Vector(1, 3, 4)
w = Vector(4, -2, 1)
v3 = find_axis(v, w)
print(v3)   