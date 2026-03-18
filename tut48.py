# ceil and floor of sorted array
nums = [1, 1, 2, 3, 4, 4, 5,6,  8, 9,10,11]
n = len(nums)
ceil = -1
floor = -1
high = n-1
low = 0
target = 10
while low <= high:
    mid = low+(high-low) //2
    if nums[mid] == target:
        floor = nums[mid]
        ceil = nums[mid]
        break
    elif nums[mid] < target:
        floor = nums[mid]
        low = mid+1
    else:
        ceil = nums[mid]
        high = mid-1

print("ceil,floor:",ceil,floor)