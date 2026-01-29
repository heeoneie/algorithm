import math

def solution(fees, records):
    answer = []
    in_time = {}
    total_time = {}
    for record in records:
        time, car_num, types = record.split()
        h, m = map(int, time.split(":"))
        minutes = h * 60 + m
        if types == "IN":
            in_time[car_num] = minutes
        else:
            diff = minutes - in_time[car_num]
            if car_num in total_time:
                total_time[car_num] += diff
            else:
                total_time[car_num] = diff
            del in_time[car_num]
    # in_time에 존재하면 그 차는 23:59으로 계산해서 total_time 추가
    for car_num in in_time:
        diff = 23 * 60 + 59 - in_time[car_num]
        if car_num in total_time:
            total_time[car_num] += diff
        else:
            total_time[car_num] = diff
    # 차 번호로 오름차순 정렬 후 요금 계산
    for car_num in sorted(total_time.keys()):
        time = total_time[car_num]
        if time <= fees[0] :
            fee = fees[1]
        else:
            fee = fees[1] + math.ceil((time - fees[0]) / fees[2]) * fees[3]
        answer.append(fee)
    return answer