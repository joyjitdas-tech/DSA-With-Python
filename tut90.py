#Infix to postfix

def preference(op):
    if op == '^':
        return 3
    elif op == '*' or op == '/':
        return 2
    elif op == '+' or op == '-':
        return 1
    else:
        return 0


def infix2postfix(s):
    stack = []
    result = []

    for ch in s:
        if ch.isalnum():
            result.append(ch)

        elif ch == '(':
            stack.append(ch)

        elif ch == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            if stack:
                stack.pop()

        else:
            while stack and preference(ch) <= preference(stack[-1]):
                result.append(stack.pop())
            stack.append(ch)

    while stack:
        result.append(stack.pop())

    return "".join(result)

def infix2prefix(s):
    # Step 1: Reverse
    s = s[::-1]

    # Step 2: Swap brackets
    s = s.replace('(', 'temp').replace(')', '(').replace('temp', ')')

    stack = []
    result = []

    for ch in s:
        if ch.isalnum():
            result.append(ch)

        elif ch == '(':
            stack.append(ch)

        elif ch == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            if stack:
                stack.pop()

        else:
            while (stack and 
                   (preference(stack[-1]) > preference(ch) )):
                result.append(stack.pop())
            stack.append(ch)

    # pop remaining
    while stack:
        result.append(stack.pop())

    # reverse final result
    return "".join(result[::-1])

def postfix2infix(s):
    stack = []

    for ch in s:
        if ch.isalnum():
            stack.append(ch)
        else:
            op2 = stack.pop()
            op1 = stack.pop()

            new = f"({op1}{ch}{op2})"

            stack.append(new)

    return stack[-1]
def prefix2infix(s):
    stack = []

    for ch in s[::-1]:
        if ch.isalnum():
            stack.append(ch)
        else:
            op1 = stack.pop()
            op2 = stack.pop()

            new = f"({op1}{ch}{op2})"

            stack.append(new)

    return stack[-1]

def postfix2prefix(s):
    stack = []
    for ch in s:
        if ch.isalnum():
            stack.append(ch)

        else:
            op2 = stack.pop()
            op1 = stack.pop()

            new = f"{ch}{op1}{op2}"
            stack.append(new)

    return stack[-1]
def prefix2postfix(s):
    stack = []
    for ch in s[::-1]:
        if ch.isalnum():
            stack.append(ch)

        else:
            op1 = stack.pop()
            op2 = stack.pop()

            new = f"{op1}{op2}{ch}"
            stack.append(new)

    return stack[-1]


s = "a+b*(c^d-e)"
s1 = "(a+b)*c-d+f"
s2 = "ab-de+f*/"
s3 = "*+pq-mn"
s4 = "ab-de+f*/"
s5 = "*+pq-mn"
print(infix2postfix(s))
print(infix2prefix(s1))
print(postfix2infix(s2))
print(prefix2infix(s3))
print(postfix2prefix(s4))
print(prefix2postfix(s5))