import sys

input = sys.stdin.readline

N = str(input().rstrip())
x = '0'

while int(x) < int(N):
    compare = 0
    for i in x:
        compare += int(i)
    if str(int(x) + compare) == N:
        break
    x = str(int(x) + 1)
if N == 1 or x == N:
    print(0)
else:
    print(int(x))

