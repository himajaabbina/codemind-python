n = int(input())
while n>9:
    s=0
    while n!=0:
        r = n%10
        n=n//10
        s+=r
    n=s
print(s)