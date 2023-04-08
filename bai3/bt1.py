so_luong_keo = int(input("Nhập số lượng kẹo của bác : "))
so_hoc_sinh = int(input("Nhập số học sinh trong lớp: "))
if so_luong_keo > so_hoc_sinh :
     so_keo_moi_hs = so_luong_keo // so_hoc_sinh
     so_keo_con_lai = so_luong_keo % so_hoc_sinh
     print("Mỗi học sinh nhận được", so_keo_moi_hs, "cái kẹo")
     print("Bác còn lại", so_keo_con_lai, "cái kẹo")
else:
    print("vì số học sinh nhiều hơn số kẹo, bác không chia nên còn nguyên số kẹo là: ",so_luong_keo,"cái kẹo" )
