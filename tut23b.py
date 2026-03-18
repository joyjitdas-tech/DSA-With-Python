# binary search

num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
key = int(input("Enter number: "))

def binary_search(arr, low, high, key):
    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == key:
            return mid
        elif key > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return -1

result = binary_search(num, key)
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")

#exponential search for creating a range for binary search it also use in sorted array

def exponential_search(arr, key):
    n = len(arr)

    if arr[0] == key:
        return 0

    i = 1
    while i < n and arr[i] <= key:
        i *= 2

    return binary_search(arr, i // 2, min(i, n - 1), key)

# result = exponential_search(num, key)
# if result != -1:
#     print("Element found at index:", result)
# else:
#     print("Element not found")