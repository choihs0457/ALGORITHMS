import sys

input = sys.stdin.readline
ans_list = set()

for _ in range(10):
    ans_list.add(int(input()) % 42)
print(len(ans_list))
