import sys

input = sys.stdin.readline

n = int(input())
command = input().rstrip()
graph = [["."] * n for _ in range(n)]
di = {"D": (1, 0), "U": (-1, 0), "R": (0, 1), "L": (0, -1)}

r, c, nr, nc = 0, 0, 0, 0
prev = ""

for i, cmd in enumerate(command):
    dr, dc = di[cmd]
    nr = r + dr
    nc = c + dc

    if 0 <= nr < n and 0 <= nc < n:
        if prev:
            if graph[r][c] == "+" or graph[nr][nc] == "+":
                prev = cmd
                r, c = nr, nc
                continue
            if prev == "D" or prev == "U":
                if cmd == "D" or cmd == "U":
                    graph[r][c] = "|"
                elif cmd == "L" or cmd == "R":
                    graph[r][c] = "+"
            elif prev == "L" or prev == "R":
                if cmd == "D" or cmd == "U":
                    graph[r][c] = "+"
                else:
                    graph[r][c] = "-"
        else:
            if cmd == "D":
                graph[r][c] = "|"
            else:
                graph[r][c] = "-"

    else:
        continue

    prev = cmd
    r, c = nr, nc

if prev:
    if graph[nr][nc] == "+":
        pass

    if 0 <= nr < n and 0 <= nc < n:
        if prev == "D" or prev == "U":
            if graph[r][c] == "-":
                graph[r][c] = "+"
            else:
                graph[r][c] = "|"
        elif prev == "L" or prev == "R":
            if graph[r][c] == "|":
                graph[r][c] = "+"
            else:
                graph[r][c] = "-"
    else:
        if cmd == "D" or cmd == "U":
            if graph[r][c] == "-":
                graph[r][c] = "+"
            elif graph[r][c] == "|":
                graph[r][c] = "|"
            elif prev != cmd:
                graph[r][c] = "-"
        else:
            if graph[r][c] == "|":
                graph[r][c] = "+"
            elif graph[r][c] == "-":
                graph[r][c] = "-"
            elif prev != cmd:
                graph[r][c] = "|"

else:
    if 0 <= nr < n and 0 <= nc < n:
        if cmd == "D" or cmd == "U":
            graph[r][c] = "|"
        else:
            graph[r][c] = "-"


for i in range(n):
    print(*graph[i], sep="")
