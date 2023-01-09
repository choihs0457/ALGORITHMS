import sys

input = sys.stdin.readline
from collections import Counter

N = int(input())

num_list = []
list_sum = 0
middle = N//2

for _ in range(N):
    num = int(input())
    num_list.append(num)
    list_sum += num

num_list.sort()
nums_s = Counter(num_list).most_common()

print(round(list_sum/N))
print(num_list[middle])
if len(nums_s) > 1:
    if nums_s[0][1] == nums_s[1][1]:
        print(nums_s[1][0])
    else:
        print(nums_s[0][0])
else:
    print(nums_s[0][0])
print(num_list[-1] - num_list[0])

