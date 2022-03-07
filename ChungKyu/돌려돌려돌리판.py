import random

def choice_one(number):
    while number != 0:
        stack_list = ['기능개발','프린터','다리를 지나는 트럭','주식가격']
        sort_list  = ['K번째 수','가장 큰 수','H-Index']
        fullSearch_list = ['모의고사', '소수 찾기', '카펫']
        greedy_list = ['체육복']

        sum_list = stack_list + sort_list + fullSearch_list + greedy_list
        sample = random.sample(sum_list, number)
        print(sample)
        number = int(input("숫자를 입력하세요 : "))
        print("끝낼려면 숫자 0을 입력하시오")

    return print("프로그램이 종료 됩니다.")



number = int(input("숫자를 입력하세요:"))
print(choice_one(number))
