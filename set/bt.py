def tbcong (a):
    tb = 0
    for i in range (len(a)):
        tb += a[i]
    tb/=(len(a))
    return tb

a = [1,2,3]
print(tbcong(a))