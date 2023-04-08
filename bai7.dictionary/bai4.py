m = int(input("nhập số n:"))
is_prime= True
if m<2:
    is_prime = False
else:
    for i in range(2,m):
        if m%i == 0:
            is_prime = False
            break
if is_prime:
    print(m,"số nguyên tố")
else:
    print("không phải số nguyên tố")
        
        