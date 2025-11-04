def min_max(x: list[int]) -> list[float]:
	# Your code here
	
    n = len(x)

    max_x = max(x)
    min_x = min(x)

    if max_x == min_x:
        return [0 for i in range(n)] 

    res = [(x[i] - min_x)/(max_x - min_x) for i in range(n)]

    return res


print(min_max([1, 2, 3, 4, 5]))