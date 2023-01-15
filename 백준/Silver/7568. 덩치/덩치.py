import sys

input = sys.stdin.readline

N = int(input())

man_list = []
ans_list = [1 for _ in range(N)]

for _ in range(N):
    weight, height = map(int, input().split())
    man_list.append([weight, height])

for x in range(N):
    for y in range(N):
        if x == y :
            continue
        if man_list[x][0] < man_list[y][0] and man_list[x][1] < man_list[y][1]:
            ans_list[x] += 1
        
for _ in ans_list:
    print(_,end=" ")

