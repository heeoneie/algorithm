'''
장르, 조회수, 고유 번호를 갖는 리스트 만듦
장르별로, 조회수 많은 순, 고유 번호로 sort

장르 별로 조회수 다 더함
장르를 조회수 별로 내림차순

장르와 처음에 만든 리스트의 장르가 같다면
cnt 증가시키고 cnt가 3이상이면 break
아니면 answer에 추가
장르의 개수만큼 반복
'''

def solution(genres, plays):
    answer = []
    best_genres = {}
    tracks = [[genres[i], plays[i], i] for i in range(len(plays))]
    tracks = sorted(tracks, key=lambda x : (x[0], -x[1], x[2]))
    
    for i in range(len(genres)):
        if genres[i] in best_genres:
            best_genres[genres[i]] += plays[i]
        else:
             best_genres[genres[i]] = plays[i]
                
    best_genres = sorted(best_genres.items(), key=lambda x:x[1], reverse=True)
    
    for genres in best_genres:
        cnt = 0
        for track in tracks:
            if genres[0] == track[0]:
                cnt += 1
                if cnt > 2:
                    break
                else:
                    answer.append(track[2])
        
    return answer