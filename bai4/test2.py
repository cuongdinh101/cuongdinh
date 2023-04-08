txt=input()
a=txt.split()
b=[]
dem2=0
for i in a:
    for y in a:
        if i==y :
            dem2+=1
    b.append(dem2)
    dem2=0
tmp=b[0]
dem3=0
dem4=-1
for i in b:
    dem4+=1
    if i>=tmp:
        dem3=dem4
result=txt.rfind(a[dem3])
print("Last occurrence of Emma starts at index ",result+1)
