import sys

input = sys.stdin.readline

N = int(input())
cnt = 1

for _ in range(N):
    floor, unit, target = map(int, input().split())
    while floor < target :
        target -= floor
        cnt += 1
    print(target, end  = "")
    print('%02d' %cnt)
    cnt = 1