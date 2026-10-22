def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    # 단어에 맞으면 인덱스 번호로 치환
    for i, word in enumerate(words):
        s = s.replace(word ,str(i))
    answer = int(s)
    return answer