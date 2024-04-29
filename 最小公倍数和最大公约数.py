import random
a = random.randint(0,100)
b = random.randint(0,100)
def gcd(a,b):             #求最大公约数
    while b != 0:
        a,b = b,a % b
    return a
def lcm(a,b):
    return(a*b) // gcd(a,b)
print("a = ",a)
print("b = ",b)
print("最大公约数:",gcd(a,b))
print("最小公倍数:",lcm(a,b))