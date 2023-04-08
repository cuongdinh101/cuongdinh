txt_1 = "String29@8496"
sum= 0
count= 0
for i in range(len(txt_1)):
    if txt_1[i].isdigit():
        sum += int(txt_1[i])
        count += 1
    else:
      " "

if count > 0:
    ave = sum / count
    print("Tổng các số:", sum)
    print("Trung bình cộng các số:", ave)
else:
    print("Không có số nào trong chuỗi")