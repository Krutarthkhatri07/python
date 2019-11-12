def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(11)
mytriple=myfunc(22)


print(mydoubler(2))
print(mytriple(3))