def prime(n):
    if n<2:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        else:
            return True
def run_loop(num,x):
    while prime(num)==False:
        num+=x
    return num
n = int(input())
pp = run_loop(n,-1)
np = run_loop(n,1)
a = n-pp
b = np-n
if prime(n)==True:
    print(0)
elif a<b:
    print(a)
elif a>b:
    print(b)
elif a==b:
    print(min(a,b))