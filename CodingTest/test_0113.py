import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

num = int(input())

for _ in range(num):
    a, b = map(int, input().strip().split(' '))

    result = lcm(a, b)
    real = a * b

    if result == real:
        print("Perfect")
    else:
        print("Not even close")