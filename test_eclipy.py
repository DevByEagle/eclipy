import eclipy

collection = eclipy.Collection([1, 2, 3], [4, 5, 6], [7, 8, 9])
vec1 = collection[0]
vec2 = collection[1]
result = eclipy.dot(vec1, vec2)
print(f"Dot product of {vec1} and {vec2}: {result}")
