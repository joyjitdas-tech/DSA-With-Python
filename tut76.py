#generate all subsequence with sum=k

def subsequence_k(num, index, ans, key, subset, curr_sum):
    if curr_sum == key:
        ans.append(subset.copy())
        return
    elif curr_sum > key:
        return 
    if  index == len(num):
        return

    subset.append(num[index])
    subsequence_k(num, index+1, ans, key, subset, curr_sum + num[index])
    subset.pop()
    subsequence_k(num, index+1, ans, key, subset, curr_sum)


num = [5,9,3,4,1]
key = 9
ans = []
subset = []

subsequence_k(num,0,ans,key,subset,0)
print(ans)