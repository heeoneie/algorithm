from itertools import combinations
import sys
input = sys.stdin.readline

nine = [int(input()) for _ in range(9)]
res = list(combinations(nine,7))
for comb in res:
    if sum(comb) == 100:
        for num in comb:
            print(num)