import re
fh=open('C:/Users/kruta/OneDrive/Desktop/file.txt')
sum=0
a=list()
for line in fh:
    line = line.strip()
    y = re.findall('[0-9]+',line)
    a=a+y
for x in a:
    x=int(x)
    sum=sum+x
print(sum)
