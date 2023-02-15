n, m = map(int, input().strip().split(' '))
arr = input()

result = []  # 누적합 배열

for i in arr:
    if i == 'e':
        result.append(1)
    else:
        result.append(0)

for _ in range(m):
    l, r = map(int, input().strip().split(' '))
    l -= 1
    count = 0
    for i in range(l, r):
        count += result[i]

    print(count)
