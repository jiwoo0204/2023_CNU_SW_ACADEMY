n = int(input())  # 건물의 수
arr = list(map(int, input().strip().split(' ')))

l_count, r_count = 1, 1
l_max, r_max = arr[0], arr[-1]

for i in arr:
    if i > l_max:
        l_max = i
        l_count += 1

for i in reversed(arr):
    if i > r_max:
        r_max = i
        r_count += 1

print(l_count, end=' ')
print(r_count)
