n = int(input())
arr = list(map(int, input().strip().split(' ')))

result = []  # 누적합 배열
count = 0

for i in range(n):
    count += arr[i]
    result.append(count)

for i in range(len(result) - 1, 0, -1):
    for j in range(i - 1, -1, -1):
        result.append(result[i] - result[j])

print(max(result))
