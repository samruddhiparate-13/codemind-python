def is_prime(i):
    if i<2:
        return False
    for j in range(2,i):
        if(i%j==0):
            return False
    return True
n=int(input())
m=int(input())
for i in range(n,m):
    if(is_prime(i)):
        print(i)

