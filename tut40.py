#2d array
nums = [[0,1,2],[3,4,5],[6,7,8]]
r = len(nums)
c = len(nums[0])
# for i in range(0,r):
#     for j in range(0,c):
#         if j <= i:
#             print(nums[i][j],end=" ")
#         else:
#             print(end="  ")
#     print()


for i in range(0,r):
    for j in range(0,c):
        print(nums[j][i],end=" ")
    print()


result = [[0]*r for _ in range(c)]
print(result)