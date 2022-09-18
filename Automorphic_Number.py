num = int(input())
square = pow(num, 2)
n= pow(10, len(str(num)))
if square % n == num:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")

    