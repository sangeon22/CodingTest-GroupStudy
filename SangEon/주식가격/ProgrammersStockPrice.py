from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)

    while prices:
        time = 0
        temp = prices.popleft()
        for i in prices:
            time+=1
            print("i = ",i)
            print("temp = ",temp)
            print("time = ",time)
            print("---------")
            if i < temp:
                break
        answer.append(time)

    return answer
