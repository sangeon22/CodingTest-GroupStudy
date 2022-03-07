from  collections import deque
def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights) # 대기 트럭
    bridge = deque([0 for _ in range(bridge_length)]) # 다리를 건너는 트럭
    time = 0
    bridge_weight =  0  # 현재 다리위 무게  <10kg

    #bridge = [7]
    #out  =[0]
    while len(bridge) != 0:
        out = bridge.popleft()
        bridge_weight -= out
        time += 1
        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                left =truck_weights.popleft()
                bridge_weight +=left
                bridge.append(left)
            else:
                bridge.append(0)

    return time


print(solution(2,10,[7,4,5,6]))