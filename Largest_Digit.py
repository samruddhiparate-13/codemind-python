n=int(input())
l=[]
while n!=0:
    r=n%10
    n=n//10
    l.append(r)
l.sort(reverse=True)
print(l[0])