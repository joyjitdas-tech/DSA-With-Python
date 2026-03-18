#Count All Subsequences with Sum K
num = [1,3,2,1]
key = 3
def count_sub(num,key,index,subset,ans,curr_sum):
    if curr_sum == key:
        ans.append(subset.copy())
        
        return 1
        
    elif curr_sum > key:
        return 0
    if index == len(num):
        return 0
    subset.append(num[index])
    include = count_sub(num,key,index+1,subset,ans,curr_sum+num[index])
    subset.pop()
    exclude = count_sub(num,key,index+1,subset,ans,curr_sum)
    return include+exclude
ans,subset=[],[]
print(count_sub(num,key,0,subset,ans,0))
print(ans)