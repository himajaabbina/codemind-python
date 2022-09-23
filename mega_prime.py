num = int(input())
count = 0
a = 0
b = 0
for i in range(1,num+1,1):
    if num%i==0:
        count+=1
    if(count==2):
        while num!=0:
            digits = num%10
            num = num//10
            sum = 0
            for j in range(1,digits+1,1):
                if digits%j==0:
                    sum+=1
            if(sum==2):
                a+=1
            b+=1
if(a==b and count==2):
    print('Mega Prime')
elif(count>2 or a!=b):
    print('Not Mega Prime')