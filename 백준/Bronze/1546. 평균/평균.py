import sys

input = sys.stdin.readline

N = int(input())
score_list = list(map(int, input().split()))
new_score = 0
list_max = max(score_list)

for i in range(N):
    new_score += score_list[i] / list_max * 100

print(new_score / N)
