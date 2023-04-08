def sum_of_digits(n):
    """Tính tổng các chữ số của một số"""
    s = 0
    for c in str(n):
        s += int(c)
    return s

def is_prime(n):
    """Kiểm tra xem một số có phải là số nguyên tố hay không"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_smith(n):
    """Kiểm tra xem một số có phải là số Smith hay không"""
    # Tính tổng các chữ số của số n
    digits_sum = sum_of_digits(n)
    
    # Kiểm tra xem số n có phải là số nguyên tố hay không
    if is_prime(n):
        return False
    
    # Tìm các thừa số nguyên tố của số n
    prime_factors = []
    i = 2
    while n > 1:
        if n % i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i += 1
    
    # Tính tổng các chữ số của các thừa số nguyên tố
    factors_digits_sum = sum(sum_of_digits(factor) for factor in prime_factors)
    
    # So sánh tổng các chữ số của số n với tổng các chữ số của các thừa số nguyên tố
    return digits_sum == factors_digits_sum

# Nhập số cần kiểm tra từ bàn phím
n = int(input("Nhập số cần kiểm tra: "))

# Kiểm tra xem số đó có phải là số Smith hay không
if is_smith(n):
    print(n, "là số Smith")
else:
    print(n, "không là số Smith")
