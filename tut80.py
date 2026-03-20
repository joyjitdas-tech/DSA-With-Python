#Subset Sums 
nums = [1,2,3]

def subset_sum(nums,result,subset,index,sum):
    if index >= len(nums):
        result.append(sum)
        return
    subset.append(nums[index])
    subset_sum(nums,result,subset,index+1,sum+nums[index])
    subset.pop()
    subset_sum(nums,result,subset,index+1,sum)
def func(nums):
    result = []
    subset = []
    subset_sum(nums,result,subset,0,0)
    print(result)
func(nums)