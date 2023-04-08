n=  input("Nhập số muốn nhâp:")
def lap (n):
    if n==n[::-1]:
        print("trung nhau")
    else:
        print("ko trung")
lap(n)