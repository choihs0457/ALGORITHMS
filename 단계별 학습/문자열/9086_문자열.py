import sys

input = sys.stdin.readline

Case = int(input())

for _ in range(Case):
    Sample = list(map(str, input().rstrip()))
    print(Sample[0], end="")
    print(Sample[-1])