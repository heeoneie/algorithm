'''
1. commands 루프 돌리면서 i,j,k 뽑음
2. array [i-1:j]로 자르고 sort후 k-1 answer에 추가
'''
def solution(array, commands):
    answer = []
    for command in commands:
        res = array
        i,j,k = command[0], command[1], command[2]
        res = res[i-1:j]
        res.sort()
        answer.append(res[k-1])
    return answer