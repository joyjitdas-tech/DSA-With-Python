#insertion sort
num = [9,5,7,8,4,2,3,1]

def insertion_sort(num):
    n = len(num)
    for i in range(1,n):
        key = num[i]
        j = i-1
        while j >=0 and num[j] > key:
            num[j+1] = num[j]
            j-=1
        num[j+1] = key

# insertion_sort(num)
# print(num)

#desending order
def insertionDesc(num):
    n = len(num)
    for i in range(1,n):
        key = num[i]
        j = i-1
        while j>=0 and num[j] < key:
            num[j+1] = num[j]
            j-=1
        num[j+1] = key

insertionDesc(num)
print(num)