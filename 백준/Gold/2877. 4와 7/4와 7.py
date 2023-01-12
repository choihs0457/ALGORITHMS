import sys

input = sys.stdin.readline

N = format(int(input())+1, 'b')
for i in N[1:]:
    if i == '0':
        print(4,end = "")
    else:
        print(7,end = "")