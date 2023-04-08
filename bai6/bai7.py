list1=[7,10,0,9,11,0,17]
list2=[]
list1.sort()
max_count= 0
for i in range(len(list1)):
    count = list1.count(list1[i])
    if count > max_count:
        max_count = count
        list2.append(list1[i])
    elif count == max_count and list1[i] not in list2:
        list2.append(list1[i])
print(list2, max_count)
