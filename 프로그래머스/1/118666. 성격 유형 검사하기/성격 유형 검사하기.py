def solution(survey, choices):
    answer = ''
    # 첫번째 알파벳이 비동의를 받으면 +
    # 두번째 알파벳이 동의를 받으면 +
    scores = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for i, choice in enumerate(choices):
        if choice == 4:
            pass
        if choice > 4: # 오른쪽 알파벳이 +
            if survey[i][1] in scores:
                scores[survey[i][1]] += choice - 4
            else:
                scores[survey[i][1]] = choice - 4
        else:
            if survey[i][0] in scores:
                scores[survey[i][0]] += 4 - choice
            else:
                scores[survey[i][0]] = 4 - choice
    # 계산끝, 유형 별로 나누기
    if scores["R"] >= scores["T"]:
        answer += "R"
    else:
        answer += "T"
    if scores["C"] >= scores["F"]:
        answer += "C"
    else:
        answer += "F"
    if scores["J"] >= scores["M"]:
        answer += "J"
    else:
        answer += "M"
    if scores["A"] >= scores["N"]:
        answer += "A"
    else:
        answer +="N"
    return answer