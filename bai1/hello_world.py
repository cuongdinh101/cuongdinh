def hinh_vuong(canh_hv):
    return canh_hv * canh_hv

canh_hv = float(input("Nhập độ dài cạnh hình vuông: "))
don_vi= 3
(input("nhập đơn vị: "))
S =hinh_vuong(canh_hv)
if S <0:
    print("sai kết quả")
else:
    print(S)
    
print("Diện tích hình vuông là:", S,don_vi)
