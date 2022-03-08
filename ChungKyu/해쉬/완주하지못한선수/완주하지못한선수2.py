from collections import  Counter
def solution(participant, completion):

    # 1. participant 의 값을 Counter 로 변환
    part_counter=Counter(participant)
    print(type(part_counter))
    print(part_counter)
    # 2. Completion 의 값을 Counter 로 변환
    comp_counter = Counter(completion)

    answer =part_counter - comp_counter
    print(answer)
    print(answer.keys())
    print(list(answer.keys())[0])
    return list(answer.keys())[0]

print(solution(["marina", "josipa", "nikola", "vinko", "filipa"] , ["josipa", "filipa", "marina", "nikola"]))
