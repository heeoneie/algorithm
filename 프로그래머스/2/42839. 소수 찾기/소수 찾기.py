'''
입력 받은 리스트로 만들 수 있는 수를 다 만들고 그 수 중에 소수 append하고 len 리턴
'''
from itertools import permutations
def solution(numbers):
    res = set()
    ans = set()

    for i in range(1,len(numbers)+1):
        res.update(int(''.join(p)) for p in permutations(numbers, i))

    for num in res:
        if num < 2:
            continue
        if num == 2:
            ans.add(num)
        isPrime = True
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                isPrime = False
        if isPrime:
            ans.add(num)

    return len(ans)