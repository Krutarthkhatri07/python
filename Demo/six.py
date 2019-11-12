count=dict()
line=input("enter the line")
word=line.split()
#print(word)
for name in word:
    if name not in count:
        count[name]=1
    else:
        count[name]=count[name]+1
for name in word:
    count[name]=count.get(name,0)+1
print(count)
print(count.keys())
for a,b in count.items():
    print(a,b)