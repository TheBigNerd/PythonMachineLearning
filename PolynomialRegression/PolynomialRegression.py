# If your data points won't fit linear regression it might be ideal to use polynomial regression
# It also uses the relationship between variables x and y to find the best way to draw a line through data points

import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

myModel = np.poly1d(np.polyfit(x, y, 3))
myLine = np.linspace(1, 22, 100)

plt.scatter(x, y)
plt.plot(myLine, myModel(myLine))
plt.show()