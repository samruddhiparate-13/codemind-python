n=int(input())
c=0
a=0
b=1
while True:
   if b>n:
       break
   else:
       c=a+b
       a=b
       b=c
if n-a>b-n:
    print(b)
elif(n-a==b-n):
    print(a,b)
else:
    print(a)