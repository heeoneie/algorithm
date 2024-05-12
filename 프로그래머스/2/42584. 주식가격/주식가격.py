'''
prices의 앞에 가격 하나 빼서 순회하면서 비교
cnt += 1 증가시키고 추출한 가격이 크다면 break하고
answer에 추가
'''
from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:
        temp = prices.popleft()
        cnt = 0
        for price in prices:
            cnt += 1
            if temp > price:
                break
        answer.append(cnt)
    return answer