a,b=map(int,input().split())
c=0
for i in range(1,min(a+1,b+1)):
    if(a%i==0 and b%i==0):
        if(c<i):
            c=i
print(c)