n = int(input())
sum = 0 
product = 1
while n>0:
    digit = n%10
    sum = sum+digit
    product = product*digit
    n = n//10
if(sum == product):
    print("Spy Number")
else:
    print("Not Spy Number")