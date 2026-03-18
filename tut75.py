#print all the subsequence
num = [1,2,3]
result = []
def subsequence(index,subset):
    
    if index == len(num):
        result.append(subset.copy())
        return 
    subset.append(num[index])
    subsequence(index+1,subset)
    subset.pop()
    subsequence(index+1,subset)
subset = []
subsequence(0,subset)
print(result)