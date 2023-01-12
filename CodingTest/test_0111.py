num = int(input())

for _ in range(num):
    n, m, k = map(int, input().strip().split(' '))
    # n = 주어지는 n일간의 주가
    # m = 구매 가격보다 m 이상 올랐을 때 판매
    # k = 구매 일자
    arr = list(map(int, input().strip().split(' ')))
    price = arr[k - 1]

    result = 0
    for i in range(k, n):
        if arr[i] >= price + m:
            result = i + 1
            break

    if result > 0:
        print(result)
    else:
        print("JB")