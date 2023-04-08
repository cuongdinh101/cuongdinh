doc =[1,2,3,4,6,7,8]

doc.sort()
for i in range(len(doc)-1):
   if( doc[i+1] != doc[i]+1 ):
       so_thieu = doc[i]+1
       print("Số bị thiếu là:",so_thieu)
   

