#check a string is palindrome or not
s = "nitirn"
a = s
l=0
r = len(s)-1
def reverse(a,l,r):
    if l>= r:
        return True
    if s[l] != s[r]:
        return False
    else:
        return reverse(a,l+1,r-1)

if reverse(a,l,r) == True:
    print("palindrome")
else:
    print("not")