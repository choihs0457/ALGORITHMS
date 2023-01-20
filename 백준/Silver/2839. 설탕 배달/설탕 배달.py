import sys

input = sys.stdin.readline

sugar_weigt = int(input())

count = 0
while sugar_weigt >= 0 :
    if sugar_weigt % 5 == 0 :
        count += (sugar_weigt // 5)
        print(count)
        break
    sugar_weigt -= 3  
    count += 1
else :
    print(-1)