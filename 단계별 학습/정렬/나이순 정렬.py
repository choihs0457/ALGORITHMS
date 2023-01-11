import sys

input = sys.stdin.readline

N = int(input().rstrip())
ans_dict = {}

for i in range(N) :
  x, y = map(str, input().rstrip().split())
  x = int(x)
  ans_dict[y] = x

sorted_dict = sorted(ans_dict.items(), key = lambda item: item[1])
for j in sorted_dict:
  print(j[1],j[0])
