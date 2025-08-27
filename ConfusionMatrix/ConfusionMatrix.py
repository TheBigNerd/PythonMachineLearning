# A confusion matrix is a table used in classification problems to assess where errors in a model were made
import numpy as np
import matplotlib.pyplot as plt

actual = np.random.binomial(1, 0.9, 1000)
predicted = np.random.binomial(1, 0.9, 1000)

from sklearn import metrics

confusion_matrix = metrics.confusion_matrix(actual, predicted)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [0, 1])

cm_display.plot()
plt.show()

# It can be used to predict accuracy

Accuracy = metrics.accuracy_score(actual, predicted)
print(Accuracy)

# Precision = Of the positives predicted, what percent is truly positive

Precision = metrics.precision_score(actual, predicted)
print(Precision)

# Sensitivity (Recall) = Of all the positive cases, what percentage are predicted positive
# Measures how good a model is at predicting positives

Sensitivity = metrics.recall_score(actual, predicted)
print(Sensitivity)

#Specifity = How well the model is at predicting negative results

Specificity = metrics.recall_score(actual, predicted, pos_label=0)
print(Specificity)

# F-Score = 'Harmonic mean' of precision and sensitivity - considering both false positive and false negative and
# is good for imbalanced datasets

F1_score = metrics.f1_score(actual, predicted)
print(F1_score)