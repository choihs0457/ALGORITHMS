import sys

input = sys.stdin.readline

point_x = set()
point_y = set()
pointer_x = [0 for _ in range(1001)]
pointer_y = [0 for _ in range(1001)]


for _ in range(3):
    N, M = map(int,input().split())
    point_x.add(N)
    point_y.add(M)
    pointer_x[N] += 1
    pointer_y[M] += 1

for x in point_x:
    if pointer_x[x] == 1:
        print(x, end=" ")
        break
for y in point_y:
    if pointer_y[y] == 1:
        print(y)
        break