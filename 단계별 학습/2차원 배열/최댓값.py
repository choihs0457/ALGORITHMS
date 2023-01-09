import sys

input = sys.stdin.readline


value_list = []
max_value = -1
target = []

for i in range(9):
    value_list = list(map(int, input().split()))
    if max_value < max(max_value, max(value_list)):
        max_value = max(max_value, max(value_list))
        target = [i+1,value_list.index(max_value)+1]
print(max_value)
for j in target:
    print(j,end = " ")