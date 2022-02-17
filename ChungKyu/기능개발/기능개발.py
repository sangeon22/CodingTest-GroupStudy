def solution(progresses, speeds):

    answer = []
    days = 0
    count = 0

    while len(progresses) != 0:
        if progresses[0] + days * speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
            print (count)
        else:
            if count > 0:
                answer.append(count)
                count = 0
            days += 1


    answer.append(count)

    print(answer)
    return answer

p = [93,30,55]
s = [1,30,5]
solution(p, s)

ck = [1]
ck.append(1)
print(ck)
