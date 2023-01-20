import sys

input = sys.stdin.readline

N = int(input().rstrip())
ans_list = []

for i in range(N) :
  x, y = map(int, input().rstrip().split())
  ans_list.append((x,y))

ans_list.sort()

for x,y in ans_list :
  print(x,y)