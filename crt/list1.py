#apart from python we can use this method for single line

l=list(input().split())
l[0],l[-1]=l[-1],l[0]
print(l)




#or universal way to solve for multiple lines
l=list(input().split())
temp=l[0]
l[0]=l[-1]
l[-1]=temp
print(l)
