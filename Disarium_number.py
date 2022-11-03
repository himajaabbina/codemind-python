num = int(input())
ans = 0
digits = len(str(num))
temp = num
while (temp != 0):
    remainder = temp % 10.
    ans = ans + remainder**digits
    digits = digits - 1
    temp = temp//10
if(num == ans):
    print("True")
else:
    print("False")