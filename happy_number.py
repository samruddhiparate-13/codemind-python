n=int(input())
s=0
while n>0:
    r=n%10
    n=n//10
    s+=r**2
    if(s>9 and n==0):
        n=s
        s=0
if s==1 or s==7:
    print("True")
else:
    print("False")