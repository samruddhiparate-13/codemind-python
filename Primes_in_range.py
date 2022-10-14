from math import sqrt
def is_prime(i):
    if i<2:
        return False
    for j in range(2,int(sqrt(i)+1)):
        if(i%j==0):
            return False
    return True
m=int(input())
n=int(input())
c=0
for i in range(m,n+1):
    if(is_prime(i)):
        c+=1
print(c)