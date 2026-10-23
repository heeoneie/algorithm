# 2 5 3 인 경우 슬라이싱과 인덱싱을 어떻게 할 건가
# 2번째와 5번째니까 array[i-1:i+1] 정렬 후 k-1번째
def solution(array, commands):
    answer = []
    for c in commands:
        i,j,k = c[0]-1, c[1], c[2]-1
        answer.append(sorted(array[i:j])[k])
    return answer