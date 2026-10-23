from collections import Counter
def solution(k, tangerine):
    answer = 0
    cnt = Counter(tangerine)
    for i in sorted(cnt.values(), reverse = True):
        if k > 0:
            k = k - i
            answer += 1
    return answer