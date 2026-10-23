# 숫자뽑기
# 뽑은 숫자 소수 인지
from itertools import permutations
def solution(numbers):
    answer = 0
    temp = set()
    for i in range(1, len(numbers)+1):
        for t in permutations(numbers, i):
            temp.add(int(''.join(t)))

    for j in temp:
        if j > 1:
            for k in range(2, j):
                if j%k == 0:
                    break
            else:
                answer += 1
    return answer 