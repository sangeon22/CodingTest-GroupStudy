def solution(brown, yellow):
    answer = []
    sum = (brown+4)//2

    for y in range(3,sum+1):
        x = sum -y
        print(x,y)
        if(x<y):
            break
        if((x-2)*(y-2)==yellow):
            answer.append(x)
            answer.append(y)
            break
    return answer