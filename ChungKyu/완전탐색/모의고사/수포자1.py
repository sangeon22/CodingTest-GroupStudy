def solution(answers):
    stu_a = [1, 2, 3, 4, 5]
    stu_b = [2, 1, 2, 3, 2, 4, 2, 5]
    stu_c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer = []
    result = [0, 0, 0]


    # [0,1],[1,2],[2,3],[3,4],[4,5]
    for idx, quiz_number in enumerate(answers):
        if quiz_number == stu_a[idx % len(stu_a)]:
            result[0] += 1
        if quiz_number == stu_b[idx % len(stu_b)]:
            result[1] += 1
        if quiz_number == stu_c[idx % len(stu_c)]:
            result[2] += 1

    maxvalue = max(result)
    for i in range(len(result)):
        if result[i] == maxvalue:
            answer.append(i+1)

    return answer