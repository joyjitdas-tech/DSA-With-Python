#count digit

num = int(input("enter the digit:"))
# count = 0
# while num > 0:
#     count +=1
#     num = num //10
# print("having total digit no:",count)

#2nd method
import math 
count = math.log10(num)+1
print("having total digit no:",int(count))