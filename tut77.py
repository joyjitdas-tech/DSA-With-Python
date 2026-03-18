#check if exist subsequence which have sum=k
num = [5,1,1,9,2,10]
key = 9
def check_sub(num,key,index,ans,subset,curr_sum):
    if curr_sum == key:
        ans.append(subset.copy())
        return True
    elif curr_sum > key:
        return False
    if index == len(num):
        return False
    subset.append(num[index])
    if check_sub(num,key,index+1,ans,subset,curr_sum+num[index]):
        return True
    subset.pop()
    return check_sub(num,key,index+1,ans,subset,curr_sum)

ans,subset = [],[]     
if check_sub(num,key,0,ans,subset,0):
    print("yes",ans)
