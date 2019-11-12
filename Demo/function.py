def fact(k):
    if(k>0):
        result=k*fact(k-1)
        #print(result)
    else:
        result=1
    return result



x=fact(5)
print(x)