n=97
flag=False
for i in range (2,n):
    if(n%i==0):
        flag=True
        break 
if(flag==True):  
    print("not a prime")
else:
    print("prime")

