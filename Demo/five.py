fh=open('C:/Users/krutarth.DESKTOP-95FD71C/Desktop/first.txt', 'r')
c=0
list1=list()
for line in fh:
    line.strip()
    if line.startswith('From '):
        x=line.split()
        if x[1] in list1:
            li=line
        else:
            list1.append(x[1])
            c=c+1
list1.sort()
print(list1)
print(c)