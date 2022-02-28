
# -*- coding: utf-8 -*-
#1. Pirme_set()을 정의한다
prime_set = set()

def isPrime(number):
    #6. 0과 1를 제외한다
    if number in (0,1):
        return False
    #7 에리토스테네스의 체
    lim = int(number ** 0.5 +1)
    for i in range(2,lim):
        if number % i  == 0:
            return False
    return True

def recursive(combination, others):
    # 5. 탈줄 조건 / 비교 조건 : 지금까지 만들어진 조합을 소수로 바꾼다.
    if combination != "":
        if isPrime(int(combination)):
         prime_set.add(int(combination))
    # 4. 현재까지 만들어진 숫자에 ,남아있느 숫자 중 하나를 더해준다.
    for i in range(len(others)):
        recursive(combination + others[i], others[:i] + others[i+1:])


def solution(numbers):

    #2. 모든 조합을 만드는 recursive를 수행한다.
    recursive("",numbers)
    #3. prime_set의 length를 반환한다.
    return  len(prime_set)


print(solution("17"))

