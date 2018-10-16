import numpy as np

tensor = np.array([[1, 2], [3, 4]])
sum_of_axis0 = np.sum(tensor, axis=0)
sum_of_axis1 = np.sum(tensor, axis=1)

print sum_of_axis0
print sum_of_axis1
