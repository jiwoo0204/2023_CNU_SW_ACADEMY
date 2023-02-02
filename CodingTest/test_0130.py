arr = input()  # 문자열

arr = arr.replace(' ', '').lower()
f = 'abcdefghijklmnopqrstuvwxyz'
flag = True

for i in f:
    if arr.find(i) == -1:
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')