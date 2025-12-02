import math

def softmax(scores: list[float]) -> list[float]:
	# Your code here

    total_sum = sum([math.exp(i) for i in scores])
    probabilities = [math.exp(i)/total_sum for i in scores]
    
    return probabilities

scores = [1, 2, 3]

print(softmax(scores))