def repeat(questionArr, q, songLength):
    for a in range(q, len(questionArr)):
        questionArr[a] -= songLength
#         전체 노래의 길이를 초과한 순간부터 맨 끝까지 길이를 빼줌으로서, 반복 재생을 구현한다.


songNum = int(input())
nameArr = [""]
timeArr = [0]

for _ in range(songNum):
    nameArr.append(input())

for _ in range(songNum):
    timeArr.append(int(input()))
    # timeArr = [0, 180, 358, 537, 722, 898]

songLength = sum(timeArr)

questionNum = int(input())
questionArr = []

for _ in range(questionNum):
    questionArr.append(int(input()))

for i in range(1, len(timeArr)):
    timeArr[i] += timeArr[i - 1]

result = []

for q in range(len(questionArr)):
    if questionArr[q] > songLength:
        repeat(questionArr, q, songLength)
    #     2, 3, 4번 반복됐을 때를 처리하는 함수 필요
    # 따라 물어보는 시간이 전체 길이를 초과할 때마다 함수를 호출하여 전체 길이를 끝까지 빼 준다.

    for i in range(len(timeArr)):
        if timeArr[i - 1] < questionArr[q] <= timeArr[i]:
            result.append(nameArr[i])

for r in result:
    print(r)
