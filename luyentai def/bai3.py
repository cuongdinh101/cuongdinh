def is_prime(x):
        count = 0
        for j in range(1, x+1):
            if x % j == 0:
                count += 1
            if count == 2:
             return False
            else:
             return True
x = int(input("nhap x = "))
print(is_prime(x))  