n = int(input())
f = 1
sum = 0
while f<n:
    if n%f==0:
        sum += f
    f+=1
if sum>n:
    print('True')
else:
    print('False')
        