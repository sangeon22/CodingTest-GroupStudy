from itertools import combinations

# [4,1,2,1]
# target = 4
# return = 2
def solution(numbers, target):
    answer = 0
    numbers.sort(reverse=True)
    # [4,2,1,1]
    total = sum(numbers)
    # sum = 8

    if (total == target):
        return 1

    # 8 > 4
    if (total > target):
        a = int((total - target) / 2)
        # a = (8-4)/2 = 2
        # [4,2,1,1] => 일부를 -로 바꿔서 total값을 target에 맞게 내려줘야함
        # [4,2,1,1] 중 -로 바꾼 number가 x라고 하면, tatal -2x 가 된다.
        # ex) 2를 -2로 바꿨다고 치면, 원래 sum = 8이지만 -2로 바꾸면 4
        # ex) 4를 -4로 바꿨다고 치면, 원래 sum = 8이자만 -4로 바꾸면 0이니까
        # 따라서 total -2x = target 이니까 x = (total - target)/2
        # 더해서 x값이 되는 값들의 부호를 -로 바꿔주면 target이 된다.
        # 더해서 x값이 되는 값들의 조합을 찾으면 됨

    # a값 이하인 값들만 저장
    # 2이하인 값들은 ? [2,1,1]
    under = []
    for i in range(len(numbers)):
        if numbers[i] <= a:
            under = numbers[i:]
            break

    # a값 이하인 값들을 합쳐서 조합하면
    #(2,) (1,1)
    for i in range(1, len(under) + 1):
        temps = combinations(under, i)
        for temp in temps:
            if sum(temp) == a:
                answer += 1
    return answer
