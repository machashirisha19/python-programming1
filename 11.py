d={1:"siri",3:1000,"varnika":2}
print(d['varnika'])
print(d.get(1))
d[5]='varnika'
print(d)
d[1]='shirisha'
print(d)
d.pop(3)
print(d)
print(d.popitem())
d.pop(6)
print(d)
d.pop("kolipaka keerthana")
print(d)
print(d.pop(3,"it died"))
d={1:"hello","good":987,123:"hi",45:'world'}
for i in d:
    # print(d.values())
    # print(d.keys())
    print(f"key:{i}")
for i in d.values():
    print(f"values:{i}")
for i,j in d.items():
    print(f"key:{i} and vlaue:{d[i]}")
str="hello world"
freq={}
for i in str:
    # if i in freq:
    #     freq[i]  += 1
    # else:
    #     freq[i] = 1
    freq[i]=freq.get(i,0)+1
print(freq)
score={'alice':90,'Bob':2,'charlie':95}
freq={}
max_score=0
char=''
for i,j in freq.items():
    if(j>max_score):
        max_score=j
        char = i
print(f'max_score of {char} is {max_score}')

# LIST INTO DICGIONARY
l1=['name','age','city']
l2=['alice',25,'new york']
d={}
for i in range(len(l1)):
    d[l1[i]]=l2[i]
print(d)
d=dict(zip(l1,l2))

print(d)
               