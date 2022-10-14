from math import sqrt
def is_prime(i):
    if i<2:
        return 0
    for j in range(2,i):
        if(i%j==0):
            return 0
    return 1
n=int(input())
c=0
for i in range(1,n+1):
    if(n%i==0 and is_prime(i)==0):
        c+=1
print(c)
