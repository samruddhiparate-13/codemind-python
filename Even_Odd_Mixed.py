n=int(input())
c=0
s=0
t=str(n)
while n!=0:
   r=n%10
   n=n//10
   if(r%2==0):
       c+=1
   elif(r%2!=0):
       s+=1
if(c==len(t)):
    print("Even")
elif(s==len(t)):
    print("Odd")
else:
    print("Mixed")