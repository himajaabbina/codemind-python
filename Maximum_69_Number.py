num = int(input())
str_n=str(num)
list_n=list(str_n)
for i in range(len(str_n)):
    if list_n[i]=="6":
       list_n[i]="9"
       break
s=''.join(list_n)
print(s)
