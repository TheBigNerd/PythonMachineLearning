# A decision Tree is a flow Chart and helps make decisions based on previous experience
import pandas as pd

df = pd.read_csv("data.csv")

# To create a decision tree all data has to be numerical
d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES':1,'NO': 2}
df['Go'] = df['Go'].map(d)

# Separate the features column from the target column

features = ['Age', 'Experience', 'Rank', 'Nationality']
X = df[features]
y = df['Go']

# Now to create the decision tree

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

tree.plot_tree(dtree, feature_names = features)
plt.show()

print(dtree.predict([[40, 10, 7, 1]]))
