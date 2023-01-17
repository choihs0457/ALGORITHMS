import sys
import math

input = sys.stdin.readline

N = int(input())

ring_list = list(map(int, input().split()))
for i in range(1, N):
    print(ring_list[0]//math.gcd(ring_list[0], ring_list[i]),end="")
    print('/', end="")
    print(ring_list[i]//math.gcd(ring_list[0], ring_list[i]))