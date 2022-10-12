n=int(input())
a=0
b=1
c=0 
d=0
while c<=n:
    c=a+b
    if(c==n):
        d=1
        break
    else:
        a=b
        b=c
if(d==1):
    print("True")
else:
    print("False")
    