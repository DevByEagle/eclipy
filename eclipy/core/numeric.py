def sqrt(x):
    if x < 0:
        raise ValueError("Cannot take square root of a negative number")
    guess = x / 2.0
    while guess * guess != x:
        guess = (guess + x / guess) / 2.0
    return guess

def dot(vec1, vec2):
    return sum(a * b for a, b in zip(vec1, vec1))

__all__ = [
    'sqrt',
    'dot'

]
