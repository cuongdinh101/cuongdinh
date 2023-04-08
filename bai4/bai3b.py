tx1 = 'Anna'
tx2 = 'kevin'
l = len(tx1)
mi = l // 2 
tx3 = ""
if l % 2 == 0:
    
    tx3 = tx1[mi-1:mi+1] + tx2 + tx1[mi:mi+2]
else:
   
    tx3 = tx1[mi] + tx2 + tx1[mi]

print(tx3)
