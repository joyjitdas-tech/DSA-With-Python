#largest eliment
num = [1,2,3,4,-5,6,17,8,9,10,11,12,13,14,15]

largest = num[0]
n=len(num)
for i in range(1,n):
    if num[i]>largest:
        largest = num[i]
print("largest is:",largest)