'''
딕셔너리 만들어서 key는 의상 이름, value는 종류
value의 개수 + value당 key 하나씩 조합
부분 집합
'''
def solution(clothes):
    hash_dict = {}
    
    for cloths in clothes:
        if cloths[1] in hash_dict:
            hash_dict[cloths[1]] += [cloths[1]]
        else:
            hash_dict[cloths[1]] = [cloths[1]]
            
    answer = 1
    for _, cloths_name in hash_dict.items():
        answer *= len(cloths_name) + 1
        
    return answer - 1