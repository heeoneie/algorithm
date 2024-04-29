'''
가질 수 있는 포켓몬 = len(nums)//2 or len(set(nums))
'''
def solution(nums):
    answer = 0
    cnt = len(nums)//2
    poketmon = set(nums)
    
    if cnt >= len(poketmon):
        answer = len(poketmon)
    else:
        answer = cnt
    return answer
