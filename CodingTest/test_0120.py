arr = list(input())

f_count = 0

for i in arr:
    if i == '1':
        f_count += 1

if f_count == 0:
    print(5)
else:
    print(f_count)