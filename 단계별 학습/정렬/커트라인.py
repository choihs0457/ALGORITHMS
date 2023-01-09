import sys

input = sys.stdin.readline

N, M = map(int, input().split())

score = []

score = list(map(int, input().split()))

print(sorted(score)[-M])
