import sys
import math

input = sys.stdin.readline

N = int(input())
cnt = 0
for i in str(math.factorial(N))[::-1]:
    if int(i) != 0:
        break
    else:
        cnt += 1
print(cnt)