#smith
x =0
y =0
import math
def is_prime(x):
    primes =[]
    for num in range(2,x+1):
        is_prime = True
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
                primes.append(num)
    return primes            

def is_prime2(y):
    prime2 = []
    for num in range(2,y+1):
        is_prime2 = True
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                is_prime2 = False
                break
        if is_prime2:
            prime2.append(num)
def is_smith(n):
    n1 = 0
    while n > 0:
        n1 += n% 10
        n//=10
    return(n1)   
    n= x*y
     
     
print(is_prime(100))
print(is_prime2(100))
n = int(input("n ="))
print(is_smith(n))
        