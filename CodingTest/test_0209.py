n, m = map(int, input().strip().split(' '))
arr = input()

f = [(1 if arr[i] == 'e' else 0) for i in range(n)]

for _ in range(m):
    l, r = map(int, input().strip().split(' '))
    l -= 1
    count = 0
    for i in range(l, r):
        count += f[i]
    print(count)
