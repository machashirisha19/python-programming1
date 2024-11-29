l=[4,7,1,8,3]
print(sum(l))
#or
sum=0
for item in l:
    sum=sum+item
print(sum)

l=[5,10,15,20]
x=15 in l
print(x)
#or by using if else statement nd index
if (l[2]==15):
    print(True)
else:
    print(False)
#or
target=32
flag=False
for item in l:
    if(item==target):
        flag=True
        break
if(flag==True):
    print(True)
else:
    print(False)        
#rev of list
l=[1,2,3,4,5]
l[::-1]
l.reverse()
print(l) 
#or
l=[1,2,3,4,5]
low=0
high=len(l)-1
while(low<high):
        l[low],l[high]=l[high],l[low]
        low=low+1
        high=high-1
print(l)

#sort and print rev 
l=[12,45,23,89,56]
l.sort()
l.reverse()
print(l)
#or
l.sort(reverse=True)
print(l)