list1 = [7, 10, 0, 9, 11, 0, 17]
list2 = []
for i in list1:
    if i == 0:
        list2.append(i)
while 0 in list1:
 list1.remove(0) 
list1.extend(list2)
print(list1)
