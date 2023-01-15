import sys

input = sys.stdin.readline

N, M = map(int, input().split())

num_list = list(map(int, input().split()))
ans = 0
for x in range(N-2):
    for y in range(x+1,N-1):
        for z in range(y+1,N):
            if num_list[x]+num_list[y]+num_list[z] <= M:
                ans = max(ans, num_list[x]+num_list[y]+num_list[z])

print(ans)
