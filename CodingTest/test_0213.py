n = int(input())
result = []

for _ in range(n):
    arr = list(input().strip().split(' '))
    if len(arr) == 2:
        # push
        result.append(arr[1])
    else:
        if len(result) == 0:
            print(-1)
        else:
            print(result.pop())