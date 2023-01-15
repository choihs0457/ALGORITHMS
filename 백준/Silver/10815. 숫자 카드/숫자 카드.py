import sys
import bisect

input = sys.stdin.readline

N = int(input())
target = sorted(list(map(int, input().split())))
M = int(input())
get = list(map(int, input().split()))

for x in get:
    if bisect.bisect_right(target,x) == bisect.bisect_left(target,x):
        print(0, end=" ")
    else:
        print(1, end=" ")