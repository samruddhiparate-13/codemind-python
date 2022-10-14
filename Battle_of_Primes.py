def is_prime(d):
    if d<2:
        return False
    for i in range(2,d):
        if(d%i==0):
            return False
    return True
n1=int(input())
n2=int(input())
i=1
while True:
    d=n1+n2+i
    if(is_prime(d)):
        print(i)
        break
    i+=1
        