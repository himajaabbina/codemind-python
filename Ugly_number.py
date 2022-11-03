def is_ugly(num):
        if num == 0:
            return False
        for i in [2, 3, 5]:
            while num % i == 0:
                num =num/i
        return num == 1
n = int(input())
ans = is_ugly(n)
if ans ==  True:
    print("Ugly Number")
else:
    print("Not Ugly Number")