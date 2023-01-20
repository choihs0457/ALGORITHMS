import sys

input = sys.stdin.readline

N, M = map(int, input().split())

F_list = []
S_list = []


for x in range(N):
    F_list.append(list(map(int, input().split())))

for y in range(N):
    S_list.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        F_list[i][j] += S_list[i][j]
for i in F_list :
    for j in i:
        print(j,end=" ")
    print()