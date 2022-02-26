#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    # print(truck_weights)

    # 다리를 건너는 트럭 [0,0]
    bridge = deque([0 for _ in range(bridge_length)])
    time=0
    # 현재 다리를 건너는 트럭 총 무게
    bridge_weights = 0

    while len(bridge) !=0:
        out = bridge.popleft()
        bridge_weights -= out
        time += 1
        if truck_weights:
            if bridge_weights + truck_weights[0] <= weight:
                temp = truck_weights.popleft()
                bridge_weights += temp
                bridge.append(temp)
            else:
                # [0,7]인경우 [7] -> [] 그러면 while문 탈출, 그니까 뒤에 0을 계속
                bridge.append(0)
    return time
