# Count Occurrences in Sorted Array

num = [1,2,3,4,4,5,7,7,8,8,10]
n = len(num)

def low_bound(num, key):
    lb = -1
    low = 0
    high = n - 1
    
    while low <= high:
        mid = low + (high - low)//2
        
        if num[mid] >= key:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return lb


def upper_bound(num, key):
    ub = n
    low = 0
    high = n - 1
    
    while low <= high:
        mid = low + (high - low)//2
        
        if num[mid] > key:
            ub = mid
            
            high = mid - 1
        else:
            low = mid + 1
            
    return ub


lower = low_bound(num,10)
upper = upper_bound(num,10)

if upper == lower and lower == -1:
    print("not exsit")

else:
    print("occur time:",upper-lower)