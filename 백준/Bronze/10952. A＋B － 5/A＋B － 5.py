import sys

input = sys.stdin.readline

while 1:
    ans = sum(map(int, input().split()))
    if not ans:
        break
    print(ans)
