n = int(input())  # 배열의 크기
arr = list(map(int, input().strip().split(' ')))  # 밥알 개수 저장

for i in range(n):
    arr[i] = abs(arr[i] - 320)

index = arr.index(min(arr))

print(index + 1)
