N = int(input())
large = 0
while N>0:
    digit = N%10
    if large<=digit:
        large = digit
    N = N//10
print(large)