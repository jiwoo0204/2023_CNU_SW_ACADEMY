case = int(input())

for _ in range(case):
    num = int(input())
    arr = list(map(int, input().split(' ')))
    spy = 0

    for i in range(num - 1):
        if arr[i] != arr[i + 1]:
            spy = i
            if i == num - 2:
                # 다음이 마지막 원소일 때
                if arr[i] == arr[i - 1]:
                    spy = i + 1

    print(spy + 1)