import sys

input = sys.stdin.readline

N = int(input())
floor_count = []


for _ in range(N):
    floor = int(input())
    unit = int(input())

    for _ in range(floor+1):
        floor_count.append([])

    floor_count[0] = list(range(1,unit+1))
    
    for floor_cnt in range(1, floor+1):
        for unit_cnt in range(unit):
            person = sum(floor_count[floor_cnt-1][:unit_cnt+1])
            floor_count[floor_cnt].append(person)
    
    print(floor_count[floor][unit-1])
    floor_count = []
