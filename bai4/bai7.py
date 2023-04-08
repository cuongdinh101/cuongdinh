txt_1 = input("nhập chuỗi 1")
txt_2 = input("nhập chuỗi 2")
l=len(txt_1)
for i in range(len(txt_1)):
    if txt_1[i] in txt_2[i]:
      print("có phần tử trùng là: ",txt_1[i])
    else:  
      print("ko có ký tự trùng")