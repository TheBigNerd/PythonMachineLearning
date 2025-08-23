# When data has different values, and even different measurement units it can be difficult to compare
# the answer to the problem is scaling

# A scaling method called standardisation: z = (x - u) / s
# z = the new value
# x = the original value
# u = the mean
# s = the standard deviation

# You can do this via sklearn standard scaler

import pandas as pd
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pd.read_csv("data.csv")

X = df[['Weight', 'Volume']]

scaledX = scale.fit_transform(X)

print(scaledX)

# You can use the scaled data with multiple regression for example o

y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]])

predictedC02 = regr.predict([scaled[0]])
print(predictedC02)