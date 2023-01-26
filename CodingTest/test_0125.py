n = int(input())  # 사람의 수
arr = list(map(int, input().strip().split(' ')))


for i in arr:
    less, more = 0, 0
    for j in range(n):
        if arr[j] < i:
            more += 1
        elif arr[j] > i:
            less += 1

    print(more, end=' ')
    print(less)
