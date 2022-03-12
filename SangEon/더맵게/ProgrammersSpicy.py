def solution(scoville, K):
    import heapq
    answer = 0
    #리스트를 오름차순 heapQ로 변환
    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville)>1:
            answer += 1
            #힙에서 가장 작은 값을 first, 두번째로 작은값을 second에 넣고 삭제
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            #힙에 계산한값을 삽입 및 자동 정렬
            heapq.heappush(scoville, first + second*2)
        else:
            return -1
    return answer