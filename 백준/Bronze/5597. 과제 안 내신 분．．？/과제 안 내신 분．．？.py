import sys

input = sys.stdin.readline

sample_list = list(range(1, 31))
for _ in range(28):
    sample_list.remove(int(input()))

print(sample_list[0])
print(sample_list[1])
