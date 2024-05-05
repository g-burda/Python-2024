#Excercise 9.1

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.exp(-x)
plt.plot(x, y1, label='sin(x)', color='red', linestyle="solid")
plt.plot(x, y2, label='cos(x)', color='green', linestyle="dashed")
plt.plot(x, y3, label='exp(-1)', color='blue', linestyle="dotted")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Plotting functions")
plt.legend()
plt.savefig('Homework 9_1.jpg')
plt.show()


#Excercise 9.1

import numpy as np

n = 100
random_points = np.random.rand(n, 2)
distance=np.linalg.norm(random_points, axis=1)
colors = np.where(distance < 1, 'green', 'red')
marker_areas = np.abs(random_points[:, 0]) + np.abs(random_points[:, 1])

plt.scatter(random_points[:, 0], random_points[:, 1], c=colors, s=marker_areas*1000, alpha=0.5)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Random Points')
plt.gca().set_aspect('equal', adjustable='box')
plt.savefig('Homework 9_2.jpg')
plt.show()
