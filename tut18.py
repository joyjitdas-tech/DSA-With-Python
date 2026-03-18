#fibonacci number -> 0,1,1,2,3,5,8,13,21,34
n = int(input("enter the number : "))
def fibo(n):
    if n == 0 or n ==1:
        return n
    else :
        return fibo(n-1) + fibo(n-2)
result = fibo(n)
print("the fibonachii number of",n,"is",result)