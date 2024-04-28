#Excercise 8.1
import numpy as np

a =np.linspace(0.0, 1.0, 11, dtype=float)
print(a)

b = np.zeros( (5, 6), dtype=int )
print(b)

x = complex(0, 1)
c = np.array( [x, x**2, x**3, x**4, x**5, x**6, x**7, x**8], dtype=complex )
print(c)

#Exercise 8.2
import numpy as np
v1 = np.arange(1, 21, 3)
print("v1=", v1)

v2 = v1[1::2]
print("v2=", v2)

v3 = v1[::-1]
print("v3=", v3)

#Exercise 8.3
import numpy as np

m1= np.arange(1, 41, 2).reshape(4,5)
print ("m1=", m1)

m2 = m1[:, ::-1]
print("m2=", m2)

m3 = m1[::-1, :]
print("m3=", m3)

m4 = m1[1:-1, 1:-1]
print("m4=", m4)
