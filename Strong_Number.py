N = int(input())
sum = 0
temp = N
while N >0:
    i = 1
    fact = 1
    rem = N%10
    while i<=rem:
        fact = fact*i
        i = i+1
    sum = sum+fact
    N = N//10
if(sum == temp):
    print("The number",temp,"is a strong number")
else:
    print("The number",temp,"is not a strong number")