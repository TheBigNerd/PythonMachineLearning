import matplotlib.pyplot as plt
import numpy as np

# A scatter plot = a diagram where each value in the data set is represented by a dot

# Drawing a scatter plot with matplotlib

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]

y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# You need two arrays of the same length

plt.scatter(x, y)
plt.show()

# Random data distributions

x = np.random.normal(5.0, 1.0, 1000)
y = np.random.normal(10.0, 2.0, 1000)
plt.scatter(x, y)
plt.show()