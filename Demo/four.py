fh = open('C:/Users/krutarth.DESKTOP-95FD71C/Desktop/first.txt', 'r')
list1 = list()
for line in fh:
    coll = line.split()
    for x in coll:
        if x in list1:
            print(end=" ")
        else:
            list1.append(x)
print(list1.sort())
