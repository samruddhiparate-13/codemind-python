a,b=map(int,input().split())
h=0
if(a>b):
    h=a
else:
    h=b
d=h
while True:
    if(h%a==0 and h%b==0):
        print(h)
        break
    else:
        h+=d
