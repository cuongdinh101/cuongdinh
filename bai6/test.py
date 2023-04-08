my_list =[100,1, 2, 3, 4, 5, 6, 7, 8, 9,100000]
so_lon= -float('inf')
so_lon2= -float('inf')
for i in range(len(my_list)):
    if( my_list[i] > so_lon):
        so_lon2 =so_lon
        so_lon = my_list[i] 
    elif my_list[i] != so_lon and my_list[i] > so_lon2:
           so_lon2 =my_list[i]

print(so_lon2)

    


