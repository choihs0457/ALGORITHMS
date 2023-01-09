import sys

input = sys.stdin.readline

num = []
num_sum = 0


for _ in range(5):
    num.append(int(input()))

print(sum(num)//5)
print(sorted(num)[2])