n, m = map(int, input().strip().split(' '))
arr = list(map(int, input().strip().split(' ')))

for _ in range(m):
    l, r = map(int, input().strip().split(' '))
    l -= 1
    r -= 1
    result = 0
    for i in range(l, r + 1):
        result += arr[i]
    print(result)
