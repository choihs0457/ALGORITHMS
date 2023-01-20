import sys

input = sys.stdin.readline

N = int(input())
cnt = 1
while N >= 2 :
    N = N - 6 * cnt
    cnt += 1
print(cnt)