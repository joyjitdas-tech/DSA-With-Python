#reverse an array ny recursion

list = [1,2,3,4,5,6]
right = len(list)-1
left = 0
re = []
# def reverse(list,re,right,left):
#     if right < left:
#         return
#     else:
#         re.append(list[right])
#         return  reverse(list,re,right-1,left)
# reverse(list,re,right,left)
# print(re)

#more optimal by swaping two pointer -> swap in the same array

def reverse(list,right,left):
    if left >= right :
        return
    else:
        list[left],list[right] = list[right],list[left]
        return reverse(list,right-1,left+1)
reverse(list,right,left)
print(list)