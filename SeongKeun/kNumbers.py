a = [1,5,2,6,3,7,4] 
b = [[2,5,3],[4,4,1],[1,7,3]]

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        arr = array[commands[i][0] - 1:commands[i][1]]
        print(arr)
        arr.sort()
        print(arr)
        answer.append(arr[commands[i][2]-1])
    return answer

print(solution(a,b))
