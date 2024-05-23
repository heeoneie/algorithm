'''
순열로 돌 수 있는 던전 배열을 만든 후
loop 돌려서 cnt을 배열에 추가
max(answer) 리턴
'''
from itertools import permutations
def solution(init_k, dungeons):
    answer = []
    dungeons_list = permutations(dungeons, len(dungeons))
    for dungeons in dungeons_list:
        k = init_k
        cnt = 0
        for dungeon in dungeons:
            if dungeon[0] <= k:
                k -= dungeon[1]
                cnt += 1
        answer.append(cnt)
    return max(answer)