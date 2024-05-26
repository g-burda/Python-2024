import pytest
import math
from Homework_6 import Vector

def test_repr():
    v = Vector(1, 3, 4)
    assert repr(v) == "Vector(1, 3, 4)"

def test_eq():
    v = Vector(1, 3, 4)
    w = Vector(4, -2, 1)
    assert v == Vector(1, 3, 4)
    assert v != w

def test_ne():
    v = Vector(1, 3, 4)
    w = Vector(4, -2, 1)
    assert v != w
    assert not (v != Vector(1, 3, 4))

def test_add():
    v = Vector(1, 3, 4)
    w = Vector(4, -2, 1)
    assert v + w == Vector(5, 1, 5)

def test_sub():
    v = Vector(1, 3, 4)
    w = Vector(4, -2, 1)
    assert v - w == Vector(-3, 5, 3)

def test_mul():
    v = Vector(1, 3, 4)
    w = Vector(4, -2, 1)
    assert v * w == 2

def test_cross():
    v = Vector(1, 3, 4)
    w = Vector(4, -2, 1)
    assert v.cross(w) == Vector(11, 15, -14)

def test_length():
    v = Vector(1, 3, 4)
    u = Vector(0, 0, 0)
    assert v.length() == math.sqrt(26)
    assert u.length() == 0

def test_hash():
    v = Vector(1, 3, 4)
    w = Vector(4, -2, 1)
    S = set([v, v, w])
    assert len(S) == 2

if __name__ == '__main__':
    pytest.main()