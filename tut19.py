#selection sorting
num = [9,5,7,8,4,2,3,1]

def selection_sort(num):
    n = len(num)
    for i in range(0,n):
        min_index = i
        for j in range(i+1,n):
            if num[j] < num[min_index]:
                min_index = j
        num[i],num[min_index] = num[min_index],num[i]

# selection_sort(num)
print(num)


#desending order
def selectionInDesc(num):
    n = len(num)
    for i in range(0,n):
        max_index = i
        for j in range(i+1,n):
            if num[j] > num[max_index]:
                max_index=j
        num[i],num[max_index] = num[max_index],num[i]

selectionInDesc(num)
print(num)