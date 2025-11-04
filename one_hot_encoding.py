import numpy as np
import random

def to_categorical(x, n_col=None):
	# Your code here

    unique_x = list(set(x))
    nrows = len(x)
    result = np.expand_dims(x, axis=1)

    if not n_col:
        ncol = n_col
    ncol = len(unique_x)
    result_array = np.repeat(result, ncol, axis=1)

    for i in range(nrows):
        for j in range(ncol):
            result_array[i, j] = 1 if result_array[i, j] == unique_x[j] else 0

    if n_col:
        zeros = np.zeros(nrows, dtype=int).reshape(-1, 1)
        result_array = np.hstack((zeros, result_array))

    return result_array
    
print(to_categorical(np.array([3, 1, 2, 1, 3]), 4))

#numpy_array_vstack = np.vstack((array1, array2)) 
