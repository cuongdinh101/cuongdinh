def list_primes(n):
    primes = []
    for num in range(2, n + 1):
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i) == 0:
                break
        else:
            primes.append(num)
    return primes
primes = list_primes(100)
print(primes)
