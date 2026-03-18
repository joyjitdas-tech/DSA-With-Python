#using hashing check num exsits how many times # nums having values in btwn 1-10
# nums = [5,3,2,3,1,9,7,1,3,9,6,4,10]
# m = [11,12,3,5,6,7,9,10,111]

# hash_list = [0]*11
# for num in nums:
#     hash_list[num] += 1
# for x in m:
#     if x < 0 or x > 10:
#         print(x,":",0)
#     else:
#         print(x,":",hash_list[x])


#using hashing check num exsits how many times # numbers can occur any type means from 1 to infinity -> use dict
# nums = [5,3,2,9,7,1,3,9,6,4,10,11,50,111,43,56,35,28,18]
# m = [11,12,3,5,6,7,9,10,111,35,28,18]

# hash_dict = {}

# # Create frequency dictionary
# for i in range(len(nums)):
#     hash_dict[nums[i]] = hash_dict.get(nums[i], 0) + 1

# # Check elements of m in dictionary
# for x in m:
#     if x in hash_dict:
#         print(x, "found", hash_dict[x])


#character maping a to z
s = "absvchembwhrcvzyenvce"
list1 = ['a', 'b', 'c','d','z','x','w','r','t']

hash_list = [0]*27
for ch in s:
    aschii = ord(ch)
    index = aschii - 97
    hash_list[index] += 1

for i in list1:
    aschii = ord(i)
    index = aschii - 97
    print(i,":",hash_list[index]) 