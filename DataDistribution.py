import numpy as np
import matplotlib.pyplot as plt
# Creating Big Data sets

x = np.random.uniform(0.0, 5.0, 250)
print(x)

# Visualising data using a histogram

plt.hist(x, 5)
plt.show()
