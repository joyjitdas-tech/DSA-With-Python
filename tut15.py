#find n factorial

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
    
result=fact(10)
print(result)