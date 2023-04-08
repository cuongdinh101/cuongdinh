list_1 =[-1,0,-1,2,-1,-4]
sum1=2
list_2=[]
for i in range(len(list_1)-1):
    for j in range(i+1, len(list_1)):
           if sum(list_1[i:j]) == sum1:
               list_2.append(list_1[i:j])
print(list_2)
           

    

        
