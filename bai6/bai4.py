list1 = [1, 0, -1, 0, -2, 2]
sum = 0
list2 = []

for i in range(len(list1) - 3):
    for j in range(i+1, len(list1) - 2):
        for k in range(j+1, len(list1) - 1):
            for o in range(k+1, len(list1)):
                if list1[i] + list1[j] + list1[k] + list1[o] == sum:
                    list2.append([list1[i], list1[j], list1[k], list1[o]])

print(list2)
