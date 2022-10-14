def is_prime(i):
    if i<2:
        return False
    for j in range(2,i):
        if(i%j==0):
            return False
    return True
def palin(i):
    temp=i
    r=0
    while(i):
        rem=i%10
        r=r*10+rem
        i//=10
    if(r==temp):
        return True
n=int(input())
if(n>=10 and n<=1000):
    i=n+1
    while True:
        if palin(i)and is_prime(i):
            print(i)
            break
        i+=1
    
