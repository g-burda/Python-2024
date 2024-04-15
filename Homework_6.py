import math

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

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

v = Vector(1, 3, 4)
w = Vector(4, -2, 1)
assert v != w
assert v + w == Vector(5, 1, 5)
assert v - w == Vector(-3, 5, 3)
assert v * w == 2
assert v.cross(w) == Vector(11, 15, -14)
assert v.length() == math.sqrt(26)
S = set([v, v, w])
assert len(S) == 2

print("Tests passed")