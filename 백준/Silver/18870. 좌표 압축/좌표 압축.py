# 좌표를 정렬해서 인덱스 번호를 출력
import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
res = sorted(list(set(numbers)))

dict = {res[i]: i for i in range(len(res))}

for i in numbers:
    print(dict[i], end=" ")