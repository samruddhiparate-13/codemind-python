n=int(input())
t=0
for i in range(len(str(n))):
    t+=(int(str(n)[i])**(i+1))
if(t==n):
    print("True")
else:
    print("False")