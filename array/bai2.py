import numpy as np

# tạo arr từ 1 list có sẵn ta dùng reshape

list1 = [1,2,3,4,5,6,7,8]
x= np.array(list1).reshape(2,4)
print(x)
# lưu ý số dòng và số cột nhân với nhau phải bằng số phần từ trong list
import