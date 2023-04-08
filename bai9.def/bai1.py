n = int(input("nhập giá trị của n: "))
def Giai_Thua(n):
    if( n == 1):
        return n
    else:
        return n *Giai_Thua(n-1)
print(Giai_Thua(n))