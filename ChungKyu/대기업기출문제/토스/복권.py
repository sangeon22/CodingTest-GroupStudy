# 넘버 로또

def solution(numbers):
    # result = []
    num_set = numbers.sort()
    for i in num_set:
        if(num_set[i] < num_set[i+1] and num_set[i] <= 45):


            # result.append(result[i])
            # print(result)
            return  True
        else:
            return False

    return False


print(solution[3,5,7,8])