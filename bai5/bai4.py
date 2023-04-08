list1 = ["Hello ", "take "] 
list2 = ["Dear", "Sir"]
list3= list(zip(list1,list2))
print(list3) 
for x in list1:
    for y in list2:
        print(x+y)