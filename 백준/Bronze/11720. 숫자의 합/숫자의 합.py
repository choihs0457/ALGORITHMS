import sys

input = sys.stdin.readline

N = int(input())

C = input().rstrip()
sum = 0
for _ in C:
    sum += int(_)

print(sum)
