n=int(input())
t=n
n=n*n
s=0
while n!=0:
    r=n%10
    n=n//10
    s+=r
if s==t:
    print("Neon Number")
else:
    print("Not Neon Number")