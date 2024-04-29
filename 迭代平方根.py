import math 
a=float(input('请输入>=0的实数a:'))
x=2
x=(x+a/x)/2
while (abs((x+a/x)/2-x)>10**-6):
    x=(x+a/x)/2
print(a,'的算术平方根={0:.3f}'.format(x))  #通过格式说明符.f对浮点数进行字符串格式化，f前加上保留的小数位数