Cost_sum = int(input())
N = int(input())
Cost_compare = 0

for _ in range(N):
    cost, count = map(int, input().split())
    Cost_compare += cost * count

if Cost_compare == Cost_sum:
    print("Yes")
else:
    print("No")
