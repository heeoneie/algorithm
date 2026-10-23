def solution(elements):
    # 길이가 1부터 elements까지 반복하면서 부분 수열의 개수 구함
    # 1일 때는 e[i:i+1]
    # 2일 때는 e[i:i+2]
    # 3일 때는 e[i:i+3]
    n = len(elements)
    elements *= 2
    temp = set()
    for i in range(1,n+1):
        for j in range(n):
            temp.add(sum(elements[i:i+j]))
    return len(temp)