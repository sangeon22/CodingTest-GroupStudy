participant =["leo", "kiki", "eden"]
completion = ["leo", "kiki", "eden"]

def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant [i]

    answer = ''
    return participant[len(participant)-1]

print(solution(participant,completion))