import numpy as np
import matplotlib.pyplot as plt

# How to create an array where the values are concentrated on a given value (Normal Data Distribution)
# Normal Distribution = Gaussian Data Distribution

x = np.random.normal(5.0, 1.0, 100000)

plt.hist(x, 100)
plt.show()