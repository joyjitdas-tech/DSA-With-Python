#find second largest
num = [1,2,3,4,17,6,17,8,9,10,11,12,13,14,15]

larg = float('-inf')
s_larg = float('-inf')

for i in range(0,len(num)):
    if num[i] > larg:
        s_larg = larg
        larg = num[i]
        
    elif num[i] > s_larg and num[i] != larg:
        s_larg = num[i]

print("second largest is:",s_larg)