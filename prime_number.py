n = int(input())
count=0
f=1
while f<=n:
    if n%f==0:
        count+=1
    f+=1
if count==2:
    print("prime")
else:
    print("not a prime")