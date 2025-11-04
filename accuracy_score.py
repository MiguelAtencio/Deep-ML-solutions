import numpy as np

def accuracy_score(y_true, y_pred):
	# Your code here

    n = len(y_true)
    correct_pred = y_true == y_pred
    accuracy= correct_pred.astype(int).sum()

    return accuracy / n


y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 0, 1, 0, 1])
output = accuracy_score(y_true, y_pred)
print(output)
