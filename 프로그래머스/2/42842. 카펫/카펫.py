'''
갈색으로 테두리 만들고 안에 노란색 채움
가로는 어떻게 결정하지?
노란색을 먼저 채워야 하나
노란색의 약수를 구함 ex) 24 -> 1,2,3,4,6,8,12,24
이걸로 채우고 갈새으로 테두리를 채울 수 있으면 그 약수 쌍을 리턴
'''
def solution(brown, yellow):
    answer = []
    y_width = 0
    y_height = 0
    
    for i in range(1, yellow+1):
        if yellow % i == 0:
            y_width = yellow // i
            y_height = i
        if y_width * 2 + y_height * 2 + 4 == brown:
            answer.append(y_width+2)
            answer.append(y_height+2)
            break
        answer.sort(reverse = True)
    return answer