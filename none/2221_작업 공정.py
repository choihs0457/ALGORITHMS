import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N = int(input())
boss = list(map(int, input().split()))

# 직속 부하 리스트 생성
subordinate = defaultdict(list)
for i, b in enumerate(boss):
    subordinate[b].append(i)

# 말단 직원을 담는 큐 생성
q = deque()
for i in range(N):
    if not subordinate[i]:
        q.append(i)

# 말단 직원부터 시작하여 상사들의 작업 시간 계산
time = [0] * N
while q:
    x = q.popleft()
    if boss[x] != -1:
        time[boss[x]] = max(time[boss[x]], time[x] + 1)
    for y in subordinate[x]:
        q.append(y)

# 모든 직원의 작업이 완료되는 시간
total_time = max(time)

# 해고된 직원의 수를 구하기 위해, 각 직원의 작업 완료 시간과 작업을 완료하기 위해 필요한 상사의 작업 완료 시간을 비교하여 최대값을 찾음
num_fired = 0
for i in range(N):
    if boss[i] != -1 and time[i] + 1 == time[boss[i]]:
        num_fired += 1

print(total_time)
print(num_fired)