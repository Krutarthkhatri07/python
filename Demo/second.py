c=0
sum=0.0
try:
    while(1):
        x=input("enter the number")
        if(x == 'done'):
            break
        c=c+1

        sum=sum+float(x)
    print(c,sum,sum/c)
except:
    print("enter the only number")

