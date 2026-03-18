#lower bound ->smallest index such that nums[i]>=target
nums = [1, 1, 2, 3, 4, 4, 5,6, 7, 7, 8, 9,10,11]
n = len(nums)
target = 12
lb = n
ub = n
low= 0
high = n-1
# while low<=high:
#     mid = low+(high-low) // 2

#     if nums[mid]>=target:
#         lb=mid
#         high = mid-1
#         print(lb)
#     else:
        
#         low=mid+1
# print(lb)
# if lb == n:
#     print("not possible")
# else:
#     print("index",lb)


#upper bound ->smallest index such that nums[i]>target
while low<=high:
    mid = low+(high-low) //2
    if nums[mid] > target:
        ub = mid
        high = mid-1
    else:
        low = mid+1
if ub == n:
    print("not possible")
else:
    print("index",ub)