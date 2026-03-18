#factor mapping optimal sol
nums = [1,2,5,6,11,12,5,1,1,1,3,3]

hash_map = {}
for i in range(0,len(nums)):
    hash_map[nums[i]] = hash_map.get(nums[i],0)+1
print(hash_map)