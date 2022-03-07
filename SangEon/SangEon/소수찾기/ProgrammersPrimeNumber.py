from itertools import permutations
def solution(numbers):
    answer = []
    num1 = [n for n in numbers]
    #["1","7"]
    per = []

    for i in range(1, len(numbers)+1):
        per += list(permutations(num1,i))
    num2 = [int(("").join(j)) for j in per]

    for n in num2:
        if n<2:
            continue
        check = True
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                check = False
                break
        if check:
            answer.append(n)

    return len(set(answer))