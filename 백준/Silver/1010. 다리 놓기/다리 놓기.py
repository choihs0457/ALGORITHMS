import sys
import math

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    x, y = map(int, input().split())
    ans = math.factorial(y) // (math.factorial(x) * math.factorial(y - x))
    print(ans)

    