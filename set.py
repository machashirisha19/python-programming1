#  l=[1,2,2,3,4,4]
#  s=set([1,2,2,3,4,4])
#  print(list(s))
#  A={1,2,3,4}
#  B={3,4,5,6}
#  print(A|B) 
#  print(A.union(B))
#  print(A&B)
#  print(A.intersection(B))
#  print(A-B)
#  print(A.difference(B))
#  l=[(1,2,3,4),{44,55,5,25,5,2,0}]
#  print(l[0][1])
#  print(5 in l[1])
#  a=[1,10,3,9,5]
#  b=[40,5,689,2,3,10,9]
#  c=a + b
#  print(c)
#  s=set(c)
#  print(s)
#  print(list(s))
#  D=['north','east','south','west','north','north','east']
#  D[2]='up'
#  l=D.count('north')
#  count=0
#  for item in D:
#      if (item== "north"):
#          count =count +1
#  print(count)
#  print(l)
#  print(D)
#  print(D[::-1]) 
l=['Alice','Bob','Charlie','Alice','Eve','Bob','David']
s=set(l)
print(s)
s.add('Frank')
print(s)
# print(list(s))
l=sorted(s)
print(l)