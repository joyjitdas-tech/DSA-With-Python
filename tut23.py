#quick sort
num = [9,5,7,10,6,8,4,2,3,1]

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= pivot:
            i += 1

        while i <= j and arr[j] > pivot:
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]
    return j


def quick(arr, low, high):
    if low < high:
        p_index = partition(arr, low, high)
        quick(arr, low, p_index - 1)
        quick(arr, p_index + 1, high)


quick(num, 0, len(num) - 1)
print(num)