txt_1 = 'T3H'
txt_2 = 't3h chuc ban hoc tot'
txt_1.islower()
txt_2.islower()

if txt_1.lower() in txt_2.lower():
    print("chuỗi 1 nằm trong chuỗi 2 :",txt_1)
else:
    print("chuỗi 1 không năm trong chuỗi 2")