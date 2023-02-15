arr = list(input())
result = []
flag = True

for i in arr:
    if i == '(':
        result.append(i)
    elif len(result) > 0 and i == ')':
        result.pop()
    else:
        flag = False
        break

if flag and len(result) == 0:
    print("YES")
else:
    print("NO")

