import sys
import math

input = sys.stdin.readline

N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    print(math.lcm(x, y))
