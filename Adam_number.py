def rev(N):
    rev = 0
    while N >0:
        digit = N%10
        rev = rev*10+digit
        N = N//10
    return rev
N = int(input())
s = N*N
r = rev(N)
r=r*r
sq=rev(r)
if(s==sq):
    print("True")
else:
    print("False")
        