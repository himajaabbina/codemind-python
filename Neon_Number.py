n = int(input())
sum = 0
square = n*n
temp = n
while square > 0:
    rem = square%10
    sum+=rem
    square = square//10
if(sum == temp):
    print("Neon Number")
else:
    print("Not Neon Number")