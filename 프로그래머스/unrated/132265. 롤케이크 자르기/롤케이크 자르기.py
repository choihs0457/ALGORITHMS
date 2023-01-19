def solution(topping):
    cnt = 0
    ans_list = [0 for _ in range(len(topping))]
    ans_list2 = [0 for _ in range(len(topping))]
    first_list = set()
    second_list = set()

    for x in range(len(topping)):
        first_list.add(topping[x])
        ans_list[x] = len(first_list)
    for y in range(-1,-len(topping)-1,-1):
        second_list.add(topping[y])
        ans_list2[y] = len(second_list)
    for z in range(len(topping)-1):
        if ans_list[z] == ans_list2[z+1]:
            cnt += 1

    return(cnt)