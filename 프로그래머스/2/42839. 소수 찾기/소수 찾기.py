from itertools import permutations
 # 넘버스로 만들 수 있는 숫자 케이스
        # 
    # 그 케이스들이 소수인지
        # 1을 제외하고 약수가 자기 자신과 1
        # for loop 돌릴때 나머지가 나오면 패스
def solution(numbers):
    answer = 0
    p = set()
    for i in range(1, len(numbers)+1):
        for t in permutations(numbers, i):
            p.add(int(''.join(t)))
    
    for i in p:
        if i <= 1:
            continue
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            answer += 1
    return answer