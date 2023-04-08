import numpy as np

arr = [
    [16, 4 ,7],
    [15, 8, 17],
    [16, 18, 20],
    [100 , 120, 200],
]
a=np.array(arr)
# kiêm tra mảng mấy chiều
print("số chiều của mảng là", a.ndim )

#kiểm tra chiều của mảng
print("size của mảng", a.shape)

#kiểm tra số phần tử trong mảng
print("số ký tự là", a.size)