def is_smith(num):
    # Hàm này kiểm tra xem một số có phải là số Smith hay không.
    digits_sum = sum(int(digit) for digit in str(num))
    factors_sum = sum(factorize(num))
    return digits_sum == factors_sum and digits_sum != sum(int(digit) for digit in str(2))

def factorize(num):
    # Hàm này trả về danh sách tất cả các thừa số nguyên tố của một số.
    factors = []
    d = 2
    while num > 1:
        while num % d == 0:
            factors.append(d)
            num //= d
        d += 1
        if d*d > num:
            if num > 1:
                factors.append(num)
            break
    return factors

def find_all_smiths(start, end):
    # Hàm này tìm tất cả các số Smith trong khoảng từ start đến end.
    smiths = []
    for num in range(start, end+1):
        if is_smith(num):
            smiths.append(num)
    return smiths

# Sử dụng hàm để tìm tất cả các số Smith trong khoảng từ 1 đến 1000.
print(find_all_smiths(1, 1000))
