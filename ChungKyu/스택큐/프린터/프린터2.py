def solution(priorities, location):
    answer = 0
    while True:
        max_num = max(priorities) #3
        for i in range(len(priorities)): # 4
            if max_num == priorities[i]: #  3 = 2
                answer+=1
                priorities[i] = 0
                max_num = max(priorities)
                if i == location:
                    return answer