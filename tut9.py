import math

num = int(input("eter the number:"))
result = []
for i in range(1,int(math.sqrt(num)+1)):
    if num%i == 0:
        result.append(i)
        if num//i != i:
            result.append(num//i)
result.sort()
print(result)