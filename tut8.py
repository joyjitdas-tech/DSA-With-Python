num = int(input("Enter number: "))
power = len(str(num))

total = 0
for digit in str(num):
    total += int(digit) ** power

if total == num:
    print("Armstrong")
else:
    print("Not Armstrong")


# Check Armstrong number
# num = 153
# n = num
# count = 0
# re = 0

# # Count number of digits
# while n > 0:
#     count += 1
#     n = n // 10

# n = num

# # Calculate sum of digits raised to power count
# while n > 0:
#     a = n % 10
#     re = re + a ** count
#     n = n // 10

# if re == num:
#     print("Armstrong")
# else:
#     print("Not Armstrong")
