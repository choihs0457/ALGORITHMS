import sys

input = sys.stdin.readline

windows = int(input())

now = 2
cnt = 1

while now * now <= windows:
    cnt += 1
    now += 1

print(cnt)
    