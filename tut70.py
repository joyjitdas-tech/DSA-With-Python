#bit manipulation
def convert2binary(num):
    result = ""
    while num>0:
        if num%2 == 1:
            result+="1"
        else:
            result+="0"
        num = num // 2
    result = result[::-1]
    return result

a = convert2binary(3000)
print("binary is",a)

def convert2decimal(string):
    num = 0
    power = 0
    index = len(string) - 1
    while index >= 0:
        deci = int(string[index]) * (2**power)
        num += deci
        power +=1
        index -=1

    return num

b = convert2decimal("101110111000")
print("decimal is",b)