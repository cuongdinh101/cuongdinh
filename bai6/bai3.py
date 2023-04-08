list1 = [-1, 0, 1, 2, -1, 4]
list2 = []
list3=[]
list4=[]

for i in range(len(list1) - 2):
    for j in range(i+1,len(list1) -1):
        for k in range(j+1,len(list1)):
            if list1[i] + list1[j]+ list1[k] == 0:
                list2.append([list1[i], list1[j],list1[k]])
                
print(list2)
    
    