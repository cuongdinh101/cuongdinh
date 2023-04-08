list1= [1,3,5,9,11,2,6,8,10]
list2 = [1, 3, 5,9, 11]
sum1=0
sum2=0
for i in list1:
    sum1 +=i
    i1=len(list1)
print(sum1)
print(i1)

for j in list2:
    sum2 +=j
    j1=len(list2)
print(sum2)
c =  sum1/i1
d =  sum2/j1
print(c)
print(d)
