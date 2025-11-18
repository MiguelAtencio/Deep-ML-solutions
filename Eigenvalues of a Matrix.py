def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:

    trace_values = [matrix[i][j] for j in range(len(matrix)) for i in range(len(matrix[j])) if i == j]
    trace = float(sum(trace_values))

    determinant = float(matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0])

    pos_eigenvalue = (trace + ((trace**2)-4*determinant)**(1/2))/2
    neg_eigenvalue = (trace - ((trace**2)-4*determinant)**(1/2))/2

    eigenvalues = [pos_eigenvalue, neg_eigenvalue]

    return eigenvalues


matrix = [[2, 1], [1, 2]]
print(calculate_eigenvalues(matrix))