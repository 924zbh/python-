n = -1
while n < 0:
    n = int(input("请输入非负整数n:" ))
sum = 1;i=1
while(i<=n):
    sum*=i
    i+=1
print(sum)
