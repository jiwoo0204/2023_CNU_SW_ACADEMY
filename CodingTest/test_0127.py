n = int(input())  # N * N 행렬
r1, c1, r2, c2 = map(int, input().strip().split(' '))

result = []

r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

b_r, s_r, b_c, s_c = 0, 0, 0, 0  # 더 큰 행과 열, 작은 행과 열을 저장하기 위한 변수

if r1 > r2:
    b_r = r1
    s_r = r2
elif r1 == r2:
    b_r, s_r = r1, r1
else:
    b_r = r2
    s_r = r1

if c1 > c2:
    b_c = c1
    s_c = c2
elif c1 == c2:
    b_c, s_c = c2, c2
else:
    b_c = c2
    s_c = c1

for _ in range(n):
    arr = []
    for _ in range(n):
        arr.append('*')
    result.append(arr)

for i in range(s_r, b_r + 1):
    for j in range(s_c, b_c + 1):
        result[i][j] = '.'

for i in range(n):
    for j in range(n):
        print(result[i][j], end='')
    print()
