c=[3, 0, 6, 1, 5]

def solution(citations):
    citations.sort()
    print(citations)
    for i in range(len(citations)):
        if citations[i] >= len(citations)-i :
            return len(citations)-i
    return 0

print(solution(c))
