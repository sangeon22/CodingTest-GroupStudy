def solution(prices):
    length = len(prices)

    # answer을 max값으로 초기화  
    answer = [ i for i in range (length - 1, -1, -1)]

    # 주식 가격이 떨어질 경우 찾기
    stack = [0]
    for i in range (1, length):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer


# prices = [1, 2, 3, 2, 3, 1] return [5, 4, 1, 2, 1, 0]