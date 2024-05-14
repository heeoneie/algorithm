'''
입력받은 2차원 배열을 for 돌리면서 둘 중에 큰 값, 작은 값 따로 저장하고
거기서 큰 값끼리 곱하고 리턴
'''
def solution(sizes):
    w = []
    h = []
    for size in sizes:
        w.append(max(size))
        h.append(min(size))
    return max(w) * max(h)