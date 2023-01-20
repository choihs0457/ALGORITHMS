import sys
import bisect

input = sys.stdin.readline

N = int(input())
target = sorted(list(map(int, input().split())))
M = int(input())
get = list(map(int, input().split()))
ans = []

for x in get:
    ans.append(str(bisect.bisect_right(target,x) - bisect.bisect_left(target,x)))

print(" ".join(ans))