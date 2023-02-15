case = int(input())
n_list = []
m_list = []

for _ in range(case):
    n, m = map(int, input().strip().split(' '))  # 격자의 세로, 가로 길이
    world = []  # 격자 배열

    for _ in range(n):
        line = list(input())
        world.append(line)  # 2차원 배열로 생성, n x m

    length = int(input())  # 입력의 길이
    action = list(input())  # 사용자 입력 문자열

    for i in range(n):
        for j in range(m):
            if world[i][j] == '@':  # 시작 위치 인덱스 저장하기
                idx_n = i
                idx_m = j
                break

    for a in action:
        # 인덱스 초과 혹은 '#'인지 확인하여 이동 가능할 경우 상하좌우로 이동
        if a == 'L':
            if idx_m - 1 < 0 or world[idx_n][idx_m - 1] == '#':
                continue
            else:
                idx_m -= 1
        elif a == 'R':
            if idx_m + 1 > m - 1 or world[idx_n][idx_m + 1] == '#':
                continue
            else:
                idx_m += 1
        elif a == 'U':
            if idx_n - 1 < 0 or world[idx_n - 1][idx_m] == '#':
                continue
            else:
                idx_n -= 1
        else:
            if idx_n + 1 > n - 1 or world[idx_n + 1][idx_m] == '#':
                continue
            else:
                idx_n += 1

    n_list.append(idx_n + 1)
    m_list.append(idx_m + 1)

for i in range(case):
    print(n_list[i], end=' ')
    print(m_list[i])
