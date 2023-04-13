import sys
import math

input = sys.stdin.readline

a,b = input().split()
c = math.lcm(int(a),int(b))

print(c)