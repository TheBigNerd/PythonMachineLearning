# Creating models to predict the outcome of an event, to measure models we use train/test (80% training / 20% testing)
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(2)

x = np.random.normal(3, 1, 100)
y = np.random.normal(150,40, 100) / x

plt.scatter(x, y)

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

plt.scatter(train_x, train_y)

# Fit the data (polynomial regression)

mymodel = np.poly1d(np.polyfit(train_x, train_y, 4))

myline = np.linspace(0, 6, 100)

plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()

# Testing R = Measures relationship between x and y axis

from sklearn.metrics import r2_score

r2 = r2_score(train_y, mymodel(train_x))
print(r2) # 0.79886 which is an OK relationship

# Using Test Data
r2 = r2_score(test_y, mymodel(test_x))
print(r2) # 0.809 shows that model fits the testing set well

# Predicting new values
print(mymodel(5))

