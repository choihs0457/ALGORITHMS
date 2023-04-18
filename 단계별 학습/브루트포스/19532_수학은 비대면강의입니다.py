import sys

input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())

flag = False
x = -1000

while x < 1000:
    if flag == True:
        break
    x +=1
    y = -1000
    while y < 1000:
        y += 1
        if a*x + b*y == c and d*x + e*y == f:
            print(x, y)
            flag = True
            break