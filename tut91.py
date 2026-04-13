#Next greater element->monotonic stack

num = [29,4,5,6,9,2,3,8,10]
n =len(num)
ans = [-1]*n
stack = []
for i in range(n-1,-1,-1):
    while len(stack) != 0 and stack[-1] <= num[i]:
        stack.pop()
    if len(stack) != 0:
        ans[i] = stack[-1]
    stack.append(num[i])

print(ans)

