def prime(i):
    count=0
    sum=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count!=2:
        sum+=1
    return sum
n=int(input())
l=[]
for i in range(1,n+1):
    if n%i==0:
        l.append(prime(i))
print(sum(l))