HF,sF,SF = map(int,input().split())
if HF>50 and sF>60 and SF>100:
    print(10)
elif HF>50 and sF>60:
    print(9)
elif sF>60 and SF>100:
    print(8)
elif HF>50 and SF>100:
    print(7)
elif HF>50 or sF>60 or SF>100:
    print(6)
else:
    print(5)
        