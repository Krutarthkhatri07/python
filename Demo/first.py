x=input("enter the input here")
try:
    y=int(x)
    print(y)
except:
    y=-1
if(y>0):
    print("done")
else:
    print("enter the number only")




fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    line.rstrip()
    if line.startswith("From "):
        word = line.split()
        print(word[1])
        count = count + 1
print("There were", count, "lines in the file with From as the first word")
