import sys

input = sys.stdin.readline

N = int(input().rstrip())
ans_list = []
for i in range(N) :
  x, y = map(int, input().rstrip().split())
  ans_list.append((x,y))

ans_list.sort(key=lambda x:(x[1],x[0]))

for x,y in ans_list :
  print(x,y)