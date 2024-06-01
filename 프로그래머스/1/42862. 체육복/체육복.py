'''
전처리: 여벌이 있는 학생의 체육복이 분실될 수도 있음
로직: 여벌 학생의 왼쪽 사람부터 빌려줌 없으면 오른쪽
'''
def solution(n, lost, reserve):
    lost_students = set(lost) - set(reserve)
    reserve_students = set(reserve) - set(lost)
    for reserve_student in reserve_students:
        if reserve_student-1 in lost_students:
            lost_students.remove(reserve_student-1)
        elif reserve_student+1 in lost_students:
            lost_students.remove(reserve_student+1)
    return n-len(lost_students)