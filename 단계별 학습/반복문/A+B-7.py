import sys

input = sys.stdin.readline

T_case = int(input())
count = 0
while T_case:
    T_case -= 1
    count += 1
    a, b = map(int, input().split())
    c = a + b
    print("Case #%d: %d" % (count, c))
