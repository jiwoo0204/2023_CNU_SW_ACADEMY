num = int(input())
arr = list(map(int, input().strip().split(' ')))

least = min(arr)  # 최솟값
count = 0

for i in arr:
    if i > least:
        for j in range(i - least):
            count += 1

print(count)