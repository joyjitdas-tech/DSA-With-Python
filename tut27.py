#Remove Duplicates from a Sorted Array 
num = [1,2,3,4,5,6,5,8,9,10,11,12,13,14,15]
for i in range(0,len(num)):
    for j in range(i+1,len(num)):
        if num[i] == num[j]:
            num.pop(j)

print(num)