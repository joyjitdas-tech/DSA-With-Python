#Write a recursive function to find power (xⁿ).
x = 0
n = 4

def power(x,n):
    if n == 0 :
        return 1
    if n == 1:
        return x
    else :
        return x * power(x,n-1)
    
result = power(x,n)
print(result)