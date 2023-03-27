import sys

input = sys.stdin.readline

Num, Count = map(int, input().split())

Ans_List = list(i for i in range(1, Num+1))

for _ in range(Count):
    Start, End = map(int, input().split())
    Start = Start - 1
    End = End - 1
    Mid = (Start+End)//2
    while Start <= Mid:
        Ans_List[Start], Ans_List[End] = Ans_List[End], Ans_List[Start]
        Start = Start + 1
        End = End - 1

for _ in Ans_List:
    print(_,end=" ")
