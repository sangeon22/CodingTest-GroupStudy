arr = [1, 1, 3, 3, 0, 1, 1]
# arr = [4, 4, 4, 3, 3]


def solution(arr):
    answer = []
    pre = 1000001
    for i in arr:
        if i != pre:
            answer.append(i)
            pre = i
    return answer


print(solution(arr))
