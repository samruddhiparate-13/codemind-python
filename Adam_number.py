n=int(input())
s=0
r=n*n
while n>0:
    rem=n%10
    s=s*10+rem
    n//=10
r1=s*s
s1=0
while r1>0:
    rem=r1%10
    s1=s1*10+rem
    r1//=10
if(s1==r):
    print("True")
else:
    print("False")