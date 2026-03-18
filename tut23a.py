#linear search
num = [9,5,7,1,4,7,8,4,2,3,1]
n = int(input("enter a number"))

for i in range(0,len(num)):
    if num[i]==n:
        print("yes")
        break
else:
    print("not")


    