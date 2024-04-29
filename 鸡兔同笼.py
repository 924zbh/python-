h = int(input("请输入总头数：" ))       #   h为总头数 
f = int(input("请输入总脚数(必须是偶数): " ))     #   y为总脚数
n = False
while(n == False):
    if f % 2 != 0:
        f = int(input("请输入总脚数(必须是偶数): " ))     #   y为总脚数
    else:
        n = True
answer = False
for x in range(h+1):       #   x为鸡的数量  y为兔子的数量
    for y in range(h+1):
        if x + y == h and 2 * x + 4 * y == f:
            answer = True

a = 2;b = 4               #2*x + 4*y = f   x + y = h      
x = int(2*h - f/2)
y = int(f/2 - h)
if answer == True:
    print("鸡：{0}只，兔：{1}只".format(x,y))
else:
    print("无解，请重新运行测试")
