a=int(input('请输入一个三位自然数:'))
b=a%10
c=a//10%10
d=a//100
print('百位数:',d)
print('十位数:',c)
print('个位数:',b)