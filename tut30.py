#283 leet code
def moveZeroes( nums):

    n = len(nums)
    temp =[]
    for i in range(0,n):
        if nums[i] != 0:
            temp.append(nums[i])
    k = len(temp)
    for i in range(0,n):
        if i< k:
            nums[i] = temp[i]
        else:
             nums[i] = 0

nums = [1,2,5,0,3,7,0,5,9]
moveZeroes(nums)
print(nums)