import numpy as np

def predict_logistic(X: np.ndarray, weights: np.ndarray, bias: float) -> np.ndarray:
	"""
	Implements binary classification prediction using Logistic Regression.

	Args:
		X: Input feature matrix (shape: N x D)
		weights: Model weights (shape: D)
		bias: Model bias

	Returns:
		Binary predictions (0 or 1)
	"""
	z = X @ weights + bias
	z = np.clip(z, -500, 500)
	sigmoid = 1 / (1 + np.exp(-z))
	res = np.ndarray((X.shape[1], weights.shape[0]))

print(np.array([[1, 1], [2, 2], [-1, -1], [-2, -2]]).shape[1])
