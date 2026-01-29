def solution(record):
    nickname = {}
    actions = []
    
    for r in record:
        if len(r.split()) > 2 :
            action, uid, name = r.split()
            nickname[uid] = name
        else:
            action, uid  = r.split()
            
        actions.append((uid, action))
    
    answer = []
    for uid, action in actions:
        if action == "Enter":
            answer.append(nickname[uid]+"님이 들어왔습니다.")
        elif action == "Leave":
            answer.append(nickname[uid]+"님이 나갔습니다.")
    
    return answer