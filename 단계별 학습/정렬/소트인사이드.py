import sys

input = sys.stdin.readline

word = []
word_int = []

word = list(input().rstrip())
for i in word:
    word_int.append(int(i))

word_int.sort(reverse=True)

for _ in word_int:
    print(_,end="")