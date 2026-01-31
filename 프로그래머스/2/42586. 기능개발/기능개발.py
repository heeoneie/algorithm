def solution(progresses, speeds):
    answer = []
    # 앞선 기능이 다 개발되어야 배포 가능
    # 로직 = 루프 돌면서 인덱스에 맞는 스피드 +
    # 앞에 기능이 100보다 크거나 같으면 앞에꺼 pop하고 또 그 다음 기능이 100보다 크거나 같은지 확인
    while len(progresses) > 0:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        cnt = 0
            # 그 다음 기능도 100인지 봐야하는데 그럼 계속 if문을 추가하는거니까 일반화하는 방법이 있을 것 같은데
        while len(progresses) > 0 and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        if cnt > 0:
            answer.append(cnt)
    return answer