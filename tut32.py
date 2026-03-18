#merge 2 sorted array
n1 = [1,2,3,4]
n2 = [1,2,5,6,7]
result = []
i,j =0,0

while i< len(n1) and j < len(n2):
    if n1[i] < n2[j]:
        result.append(n1[i])
        i+=1
    elif n1[i] == n2[j]:
        result.append(n1[i])
        i+=1
        j+=1
    else:
        result.append(n2[j])
        j+=1
while i< len(n1):
    result.append(n1[i])
    i+=1
while j< len(n2):
    result.append(n2[j])
    j+=1

print(result)