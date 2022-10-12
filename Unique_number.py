n=int(input())
l=[]
while n:
    r=n%10
    l.append(r)
    n//=10
if(len(set(l))==len(l)):
    print("Unique Number")
else:
    print("Not Unique Number")