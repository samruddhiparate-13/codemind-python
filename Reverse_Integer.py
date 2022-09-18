n=int(input())
s=0
t=n
if(n>0):
    while n!=0:
        r=n%10
        s=s*10+r
        n=n//10
elif(n>=(-231)):
    n=abs(n)
    while n!=0:
        r=n%10
        s=(s*10+r)
        n=n//10
if(t>0):
    print(s)
else:
    print((-1)*s)