import sys

input = sys.stdin.readline

N, M = map(int, input().split())

first_list = set()
second_list = set()

first_list = set(input().split())
second_list = set(input().split())
cnt = 0

for x in first_list:
    if x in second_list:
        cnt += 1
ans = len(first_list) + len(second_list) - cnt * 2
print(ans)