import sys

input = sys.stdin.readline

N = int(input())
cnt = list(map(int, input().split()))

print(cnt.count(int(input())))
