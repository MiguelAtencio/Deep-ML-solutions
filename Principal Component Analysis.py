import numpy as np 
def pca(data: np.ndarray, k: int) -> np.ndarray:
	
    # Standardizing the dataset
    mean_features = np.mean(data, axis=0)
    sd_features = np.std(data, axis=0)

    std_data = (data - mean_features)/sd_features

    #Calculating cov matrix
    cov_matrix = np.cov(std_data, rowvar=False)

    #Calculating eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
    
    # Sorting the eigenvalues and eigenvectors
    idx = np.argsort(eigenvalues)[::-1]
    eigenvectors_sorted = eigenvectors[:, idx]

    principal_components = eigenvectors_sorted[:, :k]

    return np.round(principal_components, 4)

data = np.array([[4,2,1],[5,6,7],[9,12,1],[4,6,7]])
k = 1


print(pca(np.array([[4,2,1],[5,6,7],[9,12,1],[4,6,7]]),2))
