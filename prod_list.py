from functools import reduce 
n=int(input())
m=list(map(int,input().split()))  
result1 = reduce((lambda x, y: x * y),m) 
print(result1) 
