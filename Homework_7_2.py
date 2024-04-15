#Excercise 7.2

import itertools
import random

print ("Infinite iterator (a) returning 0, 1, 0, 1, 0, 1, ...:")

class AIterator:
    def _01_iter_(self):
        return itertools.cycle([0, 1])

a_iter = AIterator()
_01_iter_ = a_iter._01_iter_()
for _ in range(10):
    print(next(iter(_01_iter_)))
    
print ("Infinite iterator (b) returning randomly 0 or 1 on demand:") 
class BIterator:
     def __iter__(self):
        return self

     def __next__(self):
        return random.choice([0, 1])

b_iter = BIterator()

for _ in range(10):
    print(next(iter(b_iter)))
    
print ("Infinite iterator (c) returning 0, 1, 0, -1, 0, 1, 0, -1, ...:")    
class CIterator:
    def __init__(self):
        self.cycle = itertools.cycle([0, 1, 0, -1])

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.cycle)
    
c_iter = CIterator()
for _ in range(10):
    print(next(iter(c_iter)))
