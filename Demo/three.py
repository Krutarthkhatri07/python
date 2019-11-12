fh=input("enter file here")
ip=open("C:/Users/krutarth.DESKTOP-95FD71C/Desktop/"+fh+".txt",'r')
sum=0
avg=0
c=0
for x in ip:
    if x.startswith('X-'):
        pos=x.find('0')
        k=x[pos:pos+6]
        y=float(k)
        s
        c=c+1
print('Average spam confidence:',(sum/c))