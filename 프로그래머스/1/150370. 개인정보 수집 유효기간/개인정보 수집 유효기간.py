def solution(today, terms, privacies):
    answer = []
    terms_dict = {}
    for t in terms:
        key, value = t.split()
        terms_dict[key] = int(value)
        #{'A': 6, 'B': 12}
    t_year, t_month, t_day = map(int, today.split("."))
    
    for i, p in enumerate(privacies):
        date, terms_type = p.split()
        year, month, day = map(int, date.split("."))
        
        month += terms_dict[terms_type]
        while month > 12:
            month -= 12
            year += 1
        day -= 1
        if day == 0:
            month -= 1
            day += 28
            if month == 0:
                year -= 1
                month += 12
        expire = year * 10000 + month * 100 + day
        today_num = t_year * 10000 + t_month * 100 + t_day
        if today_num > expire:
            answer.append(i+1)
    return answer