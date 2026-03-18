#Recursion using parameter
# 1)print 1 to n times

def print_x(x,n):
    if x > n :
        return
    print(x)
    print_x(x+1,n)

print_x(5,10)