#Generate All Binary Strings with no consequtive 1 and incresing order
n = int(input("Enter number of bit: "))
def solve(index,flag,number,result):
    if index >= len(number):
        result.append("".join(number))
        return result
    number[index] = "0"
    solve(index+1,True,number,result)
    if flag == True:
        number[index] = "1"
        solve(index+1,False,number,result)
        number[index] = "0"
def get_binary(n):
    number = [0]*n
    result = []
    solve(0,True,number,result)    
    print(result)

get_binary(n)