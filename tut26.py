#check array sorted or not
num = [10,2,3,3,4,5,6,7,8,9,10,11,12,13,14,15,15]

check = True
for i in range(0,len(num)-1):
    if num[i]>num[i+1]:
         check = False
if check == True:
    print("sorted")
else:
    print("not")

