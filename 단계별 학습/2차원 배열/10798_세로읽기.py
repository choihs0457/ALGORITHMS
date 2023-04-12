wordList = {}

for _ in range(5):
    word = input().rstrip()
    for i, value in enumerate(word):
        if wordList.get(i):
            values = list()
            for j in wordList[i]:
                values.append(j)
            values.append(value)
            wordList[i] = values
        else:
            wordList[i] = value
for i in wordList:
    for j in wordList[i]:
        print(j, end="")
