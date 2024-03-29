import sys
from collections import deque
input = sys.stdin.readline

def Road_search(now : int):
    checked = [False for _ in range(Node+1)]
    cnt = 0
    stack = deque([now])
    while stack:
        N = stack.pop()
        checked[N] = True
        for i in Edge[N]:
            if not checked[i]:
                if IO_list[i-1] == '0':
                    stack.append(i)
                else:
                    cnt += 1
    return cnt

Node = int(input())
IO_list = list(input().rstrip())
Edge = [[] for _ in range(Node+1)]
cnt = 0


for _ in range(Node-1):
    Start_node, End_node = map(int, input().split())
    Edge[Start_node].append(End_node)
    Edge[End_node].append(Start_node)


for i in range(1,Node+1):
    if IO_list[i-1] == '0':
        continue
    else:
        cnt += Road_search(i)

print(cnt)
