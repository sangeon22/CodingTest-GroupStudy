a=5            # 전체 학생 수
b=[2,4]        # 체육복을 잃어버린 학생 번호
c=[1,3,5]      # 여벌의 체육복이 있는 학생 번호

def solution(n, lost, reserve):
    reserve_uniq = set(reserve) - set(lost)              # 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있는 경우의 수를 위한 전처리
    lost_uniq = set(lost) - set(reserve)

    for i in reserve_uniq:                              # 좌측 먼저 함수 실행                    
        if i-1 in lost_uniq:
            lost_uniq.remove(i-1)
        elif i+1 in lost_uniq:
            lost_uniq.remove(i+1)

    answer = n - len(lost_uniq)

    return answer

print(solution(a,b,c))
