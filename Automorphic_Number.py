n=int(input())
c=0
t=n
while(n):
    n=n//10
    c+=1
s=t*t
pw=10**c
r=s%pw
if(r==t):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")