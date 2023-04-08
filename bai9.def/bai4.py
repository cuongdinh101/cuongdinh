n=[1,9,3,8,5,6,4,99,100]
def swap(n,i,j):
    n[i],n[j]= n[j],n[i]

def sap_xep(n):
    for i in range(len(n)-1):
        for j in range(i+1,len(n)):
            if n[i] > n[j] :
                swap(n,i,j)
sap_xep(n)
print(n)                