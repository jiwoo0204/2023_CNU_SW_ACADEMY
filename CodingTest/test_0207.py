n = int(input())
arr = list(map(int, input().strip().split(' ')))

result = []
count = 0

for i in range(n):
    count += arr[i]
    result.append(count)

for r in result:
    print(r, end=' ')
