def palin(i):
    temp=i
    r=0
    while(i):
        rem=i%10
        r=r*10+rem
        i//=10
    if(r==temp):
        return 1
n=int(input())
for i in range(n-1,0,-1):
    if palin(i):
        k=i
        break
for j in range(n+1,10000):
    if palin(j):
        t=j
        break
if(t-n==(n-k)):
    print(k,t)
elif(t-n<(n-k)):
    print(t)
else:
    print(k)