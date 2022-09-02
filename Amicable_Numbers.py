n = int(input())
m = int(input())
sum = 0
count = 0
for I in range (1,n):
    if n%I==0:
        sum+=I
for j in range (1,m):
    if m%j==0:
        count+=j
if sum==m and count==n:
    print("Amicable")
else:
    print("Not Amicable")