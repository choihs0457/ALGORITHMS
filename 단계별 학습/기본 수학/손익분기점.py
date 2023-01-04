import sys

input = sys.stdin.readline

static_cost, production_cost, price = map(int, input().split())

if production_cost >= price:
    print(-1)
else:
    break_even_point = static_cost // (price-production_cost) + 1
    print(break_even_point)