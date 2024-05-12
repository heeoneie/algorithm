'''
1. [0] * bridge_length
2. 현재 다리의 무게
3. truck_weights의 0번째 요소가 와도 가벼우면 0번째 트럭추가
'''
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    current_weight = 0
    
    while len(truck_weights) > 0:
        answer += 1
        current_weight -= bridge.popleft()

        if current_weight + truck_weights[0] <= weight:
            current_weight += truck_weights[0]
            bridge.append(truck_weights.popleft())
        else:
            bridge.append(0)
            
            
    answer += bridge_length
    return answer