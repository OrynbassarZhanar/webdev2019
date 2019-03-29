import math
a=int(input())
s=int()
for x in range (1,a+1):
    if a%x==0:
        s=s+1
print(s)