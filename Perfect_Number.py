def perfect(n):
    s=0
    for i in range(1,n):
        if(n%i==0):
            s+=i
    return s
n=int(input())
p=perfect(n)
if(n==p):
    print("True")
else:
    print("False")
            
