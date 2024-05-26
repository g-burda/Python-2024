import numpy as np
import matplotlib.pyplot as plt

lenght = 1.0        
time = 1.0       
number_of_points = 50       
number_of_steps = 500 
Dif_coe = 0.1
dx = lenght/ number_of_points    
dt = time / number_of_steps   

r = Dif_coe * dt / dx**2
x = np.linspace(0, lenght, number_of_points+1)
t = np.linspace(0, time, number_of_steps+1)  

u = np.zeros((number_of_points+1, number_of_steps+1))
u[:, 0] = np.sin(2 * np.pi * x)

u[0, :] = t
u[number_of_points, :] = np.exp(-t)

for j in range(number_of_steps):
    for i in range(1, number_of_points):
        u[i, j+1] = r*u[i-1, j] + (1-2*r)*u[i, j] + r*u[i+1, j]

plt.figure(figsize=(10, 6))
for i in range(0, number_of_steps+1, number_of_steps//10):
    plt.plot(x, u[:, i], label=f't={t[i]:.2f}')
plt.xlabel('x')
plt.ylabel('u(x,t)')
plt.title('1D Heat Equation')
plt.legend()
plt.grid(True)
plt.show()




import numpy as np
import matplotlib.pyplot as plt

length = 1.0        
time = 1.0       
number_of_points = 50       
number_of_steps = 500 
wave_speed = 1.0
dx = length / number_of_points    
dt = time / number_of_steps

r = (wave_speed * dt / dx) ** 2
x = np.linspace(0, length, number_of_points + 1)
t = np.linspace(0, time, number_of_steps + 1) 

u = np.zeros((number_of_points + 1, number_of_steps + 1))
u[:, 0] = np.sin(np.pi * x)

for i in range(1, number_of_points):
    u[i, 1] = u[i, 0] + (r / 2) * (u[i - 1, 0] - 2 * u[i, 0] + u[i + 1, 0])

for j in range(1, number_of_steps):
    for i in range(1, number_of_points):
        u[i, j + 1] = 2 * (1 - r) * u[i, j] + r * (u[i - 1, j] + u[i + 1, j]) - u[i, j - 1]

    u[0, j + 1] = u[1, j + 1] 
    u[number_of_points, j + 1] = u[number_of_points - 1, j + 1]  

plt.figure(figsize=(10, 6))
for i in range(0, number_of_steps + 1, number_of_steps // 10):
    plt.plot(x, u[:, i], label=f't={t[i]:.2f}')
plt.xlabel('x')
plt.ylabel('u(x,t)')
plt.title('1D Wave Equation with Neumann Boundary Conditions')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05))
plt.grid(True)
plt.show()