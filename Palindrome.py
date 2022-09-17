N = int(input())
rev = 0 
temp = N
while N>0:
    rem = N%10
    rev = rev*10+rem
    N=N//10
if (temp==rev):
    print("True")
else:
    print("False")