a = int(input())
c = 0
for x in range(a):
    b = input().split("X")
    for x in range(0, len(b)):
        for y in range(1, len(b[x])+1):
            c = c + y
    print(c)
    c = 0