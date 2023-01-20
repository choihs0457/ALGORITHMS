import sys

input = sys.stdin.readline

while 1:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break

    factor = M % N
    multiple = N % M

    if factor == 0:
        print('factor')
    elif multiple == 0:
        print('multiple')
    else:
        print('neither')

