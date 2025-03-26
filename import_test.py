import find_min_max, sum_range
import random

A = []
for _ in range(10):
    A.append(random.randint(1,100))
    
print("(min, max) =", find_min_max.find_min_max(A))
print("Sum =", sum_range.sum_range(1,10))