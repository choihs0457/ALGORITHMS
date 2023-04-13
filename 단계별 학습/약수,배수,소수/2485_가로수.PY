import sys
import math

input = sys.stdin.readline

case = int(input())
trees = []
interval = []

for _ in range(case):
    spot = int(input())
    trees.append(spot)

for i,val in enumerate(trees):
    if i == 0:
        continue
    interval.append(val-trees[i-1])

Gcd = math.gcd(*interval)
Ans = 0

for Num in interval:
    Ans += Num // Gcd - 1

print(Ans)