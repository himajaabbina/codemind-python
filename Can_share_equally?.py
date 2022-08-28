X,Y = map(int,input().split())
if (X+(Y*2))%2==0:
    if X==0 and Y%2==0:
        print('YES')
    elif X==0 and (Y)%2!=0:
        print('NO')
    else:
        print('YES')
else:
    print('NO')