def solution(citations):
    answer = 0
    citations.sort()
    print(citations)

    for i in range(1, len(citations)+1):
        min_num = citations[-i]

        if min_num >= i:
            answer = i


    return answer


print(solution([3,0,6,1,5]))