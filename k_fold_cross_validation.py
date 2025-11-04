import numpy as np

def k_fold_cross_validation(X: np.ndarray, y: np.ndarray, k=5, shuffle=True):
    """
    Implement k-fold cross-validation by returning train-test indices.
    """
    # Your code here
    n = len(X)

    indices = [i for i in range(n)]

    k_folds_indices = []

    test_start = 0
    test_step = int(n/k)
    test_end = int(n/k)

    for x in range(k):

        test_indices = indices[test_start:test_end]
        training_indices = [index for index in range(len(X)) if index not in test_indices]
        k_folds_indices.append((training_indices, test_indices))
        test_start += test_step 
        test_end += test_step

    if shuffle:
        return np.random.shuffle(k_folds_indices)

    return k_folds_indices

print(k_fold_cross_validation(np.array([0,1,2,3,4,5,6,7,8,9]), np.array([0,1,2,3,4,5,6,7,8,9]), k=5, shuffle=False))
