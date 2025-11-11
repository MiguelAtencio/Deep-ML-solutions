def conditional_probability(data, x, y):
    """
    Returns the probability P(Y=y|X=x) from list of (X, Y) pairs.
    Args:
      data: List of (X, Y) tuples
      x: value of X to condition on
      y: value of Y to check
    Returns:
      float: conditional probability, rounded to 4 decimal places
    """
    if not any(x in obs for obs in data):
        return 0.0

    count_num = 0
    count_den = 0

    for i in data:
        if (x, y) == i:
            count_num += 1
        if x == i[0]:
            count_den += 1

    return round(count_num/count_den, 4)