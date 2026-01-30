def solution(answers):
    answer = []
    a = [1,2,3,4,5] * 2000
    b = [2,1,2,3,2,4,2,5] * 1500
    c = [3,3,1,1,2,2,4,4,5,5] * 1000
    a_cnt = 0
    b_cnt = 0
    c_cnt = 0
    for i in range(len(answers)):
        # 누가 제일 많이 맞췄는지
        if answers[i] == a[i]:
            a_cnt += 1
        if answers[i] == b[i]:
            b_cnt += 1
        if answers[i] == c[i]:
            c_cnt += 1
    best = max(a_cnt, b_cnt, c_cnt)
    if a_cnt == best:
        answer.append(1)
    if b_cnt == best:
        answer.append(2)
    if c_cnt == best:
        answer.append(3)
    return answer