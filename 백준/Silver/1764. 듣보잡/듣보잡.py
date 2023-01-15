import sys

input = sys.stdin.readline

N, M = map(int, input().split())

no_listen_list = set()
ans_list = set()

for _ in range(N):
    no_listen_list.add(input().strip())
for _ in range(M):
    ans = input().strip()
    if ans in no_listen_list:
        ans_list.add(ans)

print(len(ans_list))
for _ in sorted(ans_list):
    print(_)