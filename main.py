import numpy as np

x = np.array([[78,53,27], [95,34,18], [46,39,92], [55,77,33], [69,88,25]])

print("Task - Replace all odd elements in array to -1")

print("Array before replacing:")

print(x)

print("Array after replacing:")

x[x % 2 ==1 ] = -1

print(x)
