m = int(input("nhập số n:"))
uoc_so=[]
for i in range(1,m+1):
    if m %i==0:
        uoc_so.append(i)
print(uoc_so)