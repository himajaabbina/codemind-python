def reverse(n):
    rev = 0
    while n>0:
        r = n%10
        rev = rev*10+r
        n = n//10
    return rev
n = int(input())
a = n*n
b = reverse(n)
x = b*b
y = reverse(x)
if a==y:
    print("True")
else:
    print("False")