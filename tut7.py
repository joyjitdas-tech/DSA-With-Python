#palindrome check
# number = int(input("enter the digit: "))
# num = number
# reverse = 0
# while num > 0:
#     a = num%10
#     reverse = reverse*10 + a
#     num = num // 10
# if number == reverse:
#     print("palindrome")
# else:
#     print("not palindrome")

#reverse the number
number = int(input("enter the digit: "))
num = number
reverse = 0
while num > 0:
    a = num%10
    reverse = reverse*10 + a
    num = num // 10
print(reverse)