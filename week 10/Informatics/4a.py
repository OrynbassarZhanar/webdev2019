n = int(input())
arr = []
for x in range(n):
    x = int(input())
    arr.append(x)    
for i in range (len(arr)):
    if(i%2==0):
        print(arr[i])