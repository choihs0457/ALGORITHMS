import sys
import bisect

input = sys.stdin.readline

N, M = map(int, input().split())

monster = {}

for i in range(N):
    save = input().rstrip()
    monster[save] = i
    monster[i] = save


for j in range(M):
    a = input().rstrip()
    if a.isdigit():
        print(monster[int(a)-1])
    else:
        print(monster[a]+1)
