import math
x,y=map(int,input().split())
s1=x%(10**y)
s2=x // 10 ** (int(math.log(x, 10)) - y + 1)
print(abs(s1-s2))