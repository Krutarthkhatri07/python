import urllib.request
import json
url=input("enter the url:")
data=urllib.request.urlopen(url).read().decode('utf-8')
items = json.loads(data)
sum=0
for item in items["comments"]:
    sum += int(item['count'])
print("sum",sum)

