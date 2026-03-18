#roated array
num = [1,2,3,4,5,6,5,8,9,10,11,12,13,14,15]
n = len(num)
temp = num[n-1]
for i in range(n-2,-1,-1):
    num[i+1] = num[i]
num[0] = temp
print(num)


#by slicing in python

num[:] = [num[n-1]] + num[0:n-1]
print(num)