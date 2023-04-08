import math
def is_perfect_square (n):
    if n ==1:
        return False
    else:
        return math.isqrt(n) **2 == n
    
x = [1,2,3,4,5,36,7,9,16]
prefect_square= list(filter(is_perfect_square,x))
print(prefect_square)