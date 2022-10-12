n=int(input())
for i in range(1,n+1):
    p=i*i
    if(p==n):
        break
if(p==n):
    print("True")
else:
    print("False")