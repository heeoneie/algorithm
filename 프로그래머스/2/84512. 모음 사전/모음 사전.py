'''
사전을 다 만들어 놓고 매개변수가 몇 번째 인덱스에 존재하는지
그 인덱스 +1 리턴

사전을 만드는 로직
순열로 만든 후 사전 순으로 정렬
'''
from itertools import product

def solution(word):
    words = ['A', 'E', 'I', 'O', 'U']
    dictionary = []

    for i in range(1, 6):
        for comb in product(words, repeat=i):
            dictionary.append(''.join(comb))

    dictionary.sort()
    
    return dictionary.index(word)+1