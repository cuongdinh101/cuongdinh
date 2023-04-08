a = float(input("nhập số a: "))
b = float(input("nhập số b: "))
c = float(input("nhập số c: "))
temp = float(b*b -4*a*c)
print("kết quả của denta tính được là :",temp)
if temp>0:
    print("Phương trình có 2 no phân biệt!" )
elif temp == 0:
    print("Phương trình no kép!: ")
else :
 print("Phương trình vô no: ")

