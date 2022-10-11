a=int(input())
b=int(input())
for i in range(a,b+1):
    n=i
    while n:
        r=n%10
        if(r==0 or i%r!=0):
            break
        n//=10
    else:
        print(i,end=" ")