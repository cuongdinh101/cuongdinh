nam_sinh = int(input("Nhập năm sinh :"))
nam_hien_tai=int(input("nhập năm hiện tại: "))
age= nam_hien_tai - nam_sinh
if age <0:
    print("sai rồi nhập lại đi đồng trí")
else:
    print(age)