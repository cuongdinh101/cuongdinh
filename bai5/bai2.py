list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3= list(zip(list1,list2))
print(list3) 
for x,y in list3:
    print(x+y,end =" ")