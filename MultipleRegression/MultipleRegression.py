# Multiple regression is like linear regression, but with more than one independent value, meaning
# we try to predict values based on two or more variables

import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = LinearRegression()
regr.fit(X, y)
predictCO2 = regr.predict([[2300, 1300]])
print(predictCO2)
# The coefficient is a factor that describes the relationship with an unknown variable.
print(regr.coef_)