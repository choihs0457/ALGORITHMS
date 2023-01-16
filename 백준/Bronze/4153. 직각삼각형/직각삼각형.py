import sys

input = sys.stdin.readline

while 1:
    X, Y, Z = map(int, input().split())
    if X == Y == Z == 0:
        break
    side_list = sorted([X, Y, Z])
    compare1 = 0
    compare2 = 0    

    compare1 = side_list[0]**2 + side_list[1]**2
    compare2 = side_list[2]**2
    
    if compare1 == compare2:
        print('right')
    else:
        print('wrong')

