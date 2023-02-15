arr = input()  # 문자열

arr = arr.replace(' ', '').lower()
f = 'abcdefghijklmnopqrstuvwxyz'
flag = False
result = []

for i in f:
    if arr.find(i) == -1:
        flag = True
        result.append(i)

if flag:
    print('YES')
    for r in result:
        print(r, end='')
else:
    print('NO')
