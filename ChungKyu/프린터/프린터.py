def solution(priorities, location):

    # 1 .Q를 만든다
    printer = [(i,p) for i,p in enumerate(priorities)]
    turn = 0
    while printer:
        job = printer.pop(0)
        #2. 나보다 중요한  job이 있으면 뒤에 넣는다
        if any(job[1] < other_job[1] for other_job in printer):
            printer.append(job)
        else:
            turn +=1
            #3. 너가 제일 중요하다면 수행하고 location을 비교한다.
            if job[0] == location:
                break


    return turn

print (solution([2,1,3,2],0))