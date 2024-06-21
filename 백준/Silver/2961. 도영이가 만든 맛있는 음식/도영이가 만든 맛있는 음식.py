'''
가장 차이가 적어야 함
s는 곱 b는 합
조합을 사용하여 나올 수 있는 경우의 수를 구함
조합 별로 나올 수 있는 수중에 제일 작은 수를 저장
'''
import sys
from itertools import combinations

input = sys.stdin.readline
n = int(input())
recipes = [list(map(int, input().split())) for _ in range(n)]

res = 1000000000
for i in range(1, n+1):
    for comb in combinations(recipes, i):
        sour = 1
        bitter = 0
        for recipe in comb:
            sour *= recipe[0]
            bitter += recipe[1]
        res = min(res, abs(sour-bitter))

print(res)
