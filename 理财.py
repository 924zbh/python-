a = int(input("请输入本金: "))
b = float(input("请输入年利率："))
n = 0
while(a <= 20000):
    a = a * (1 + b / 100)
    n += 1
print("{0}年后理财产品连本带息翻倍".format(n))