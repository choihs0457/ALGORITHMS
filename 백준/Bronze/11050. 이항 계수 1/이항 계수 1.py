import sys
import math

input = sys.stdin.readline

n,k = map(int, sys.stdin.readline().split())
print(math.factorial(n) // (math.factorial(k) * math.factorial(n-k)))
