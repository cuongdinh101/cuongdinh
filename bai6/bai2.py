doc = [1, 2, 3, 4, 6, 7, 10]
for i in range(len(doc)-1):
    if doc[i+1] != doc[i]+1:
        for j in range(doc[i]+1, doc[i+1]):
            print("Số thiếu là:", j)
            
