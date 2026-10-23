# 노랑 타일은 전체 타일에 가로-2 * 세로-2
def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(3, total):
        if total % i == 0:
            # 약수를 구할 수 있음
            # 1,2,3,4,6,12  
            # 가로가 i 면 세로는 total // i
            if i >= total // i:
                w = i
                h = total // i
                if (w-2) * (h-2) == yellow:
                    answer.append(w)
                    answer.append(h)
                    break
    return answer