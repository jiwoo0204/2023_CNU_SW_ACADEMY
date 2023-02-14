n, m = map(int, input().strip().split(' '))
arr = list(map(int, input().strip().split(' ')))
arr.insert(0, 0)
prefix = [0]

for i in range(1, n + 1):
    prefix.append(prefix[i - 1] + arr[i])

for _ in range(m):
    l, r = map(int, input().strip().split(' '))
    print(prefix[r] - prefix[l - 1])

