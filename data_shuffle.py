import numpy as np

def shuffle_data(X, y, seed=None):
	# Your code here

    n = len(X)
    if seed:
        np.random.seed(seed)
    
    random_index = [i for i in range(len(X))]

    np.random.shuffle(random_index)

    X_res = [X[i] for i in random_index]
    y_res = [y[i] for i in random_index]

    X_res = np.asanyarray(X_res, dtype=int)
    y_res = np.asanyarray(y_res, dtype=int)

    return X_res, y_res

X = np.array([[1, 2], 
                  [3, 4], 
                  [5, 6], 
                  [7, 8]])

y = np.array([1, 2, 3, 4])

print(shuffle_data(X, y, 42))

