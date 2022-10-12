a=int(input())
b=int(input())
c=0
d=0
for i in range(1,a):
    r=a%i
    if(r==0):
        c+=i
for i in range(1,b):
    r=b%i
    if(r==0):
        d+=i
if(c==b and d==a):
    print("Amicable")
else:
    print("Not Amicable")
    