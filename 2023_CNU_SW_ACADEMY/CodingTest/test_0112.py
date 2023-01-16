songNum = int(input())
nameArr = [""]
timeArr = [0]

for _ in range(songNum):
    nameArr.append(input())

for _ in range(songNum):
    timeArr.append(int(input()))

questionNum = int(input())
questionArr = []

for _ in range(questionNum):
    questionArr.append(int(input()))

for i in range(1, len(timeArr)):
    timeArr[i] += timeArr[i - 1]

result = []

for q in questionArr:
    for i in range(len(timeArr)):
        if timeArr[i - 1] < q <= timeArr[i]:
            result.append(nameArr[i])

for r in result:
    print(r)

