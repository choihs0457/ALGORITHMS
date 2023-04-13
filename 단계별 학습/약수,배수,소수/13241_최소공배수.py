import sys
import math

input = sys.stdin.readline

Num1,Num2 = input().split()
AnsNum = math.lcm(int(Num1),int(Num2))

print(AnsNum)