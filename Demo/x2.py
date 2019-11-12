import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')
print(type(fhand))
count=dict()
for line in fhand:
    line=line.strip()
    words=line.decode().split()
    for word in words:
        count[word]=count.get(word,0)+1
print(count)
