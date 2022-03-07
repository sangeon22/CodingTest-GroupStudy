#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque
def solution(priorities, location):
    answer = 0
    index = deque([i for i in range(len(priorities))])
    # print(index) => deque([0,1,2,3]) 인덱스 저장
    maximum = max(priorities)

    while True:
        temp = index.popleft()
        # 젤 왼쪽이니까 0번째 인덱스가 들어갈거임

        if priorities[temp] < maximum:
            index.append(temp)
            #중요도가 max보다 작으면 맨뒤로 보냄

        else:
            answer += 1
            priorities[temp] = 0
            maximum = max(priorities)
            if temp == location:
                return answer