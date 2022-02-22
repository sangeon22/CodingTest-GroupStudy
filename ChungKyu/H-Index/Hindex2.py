# -*- coding: utf-8 -*-
# a = [1.2, 2.5, 3.7, 4.6]
# a = list(map(min, a))
# print(a)

# -*- coding: utf-8 -*-
arr = ['토끼','말','늑대','오리','고양이','여우','곰']
for i,v in enumerate(arr,start= 1):
    print('number:{}, value:{}'.format(i,v))


citations =[3, 0, 6, 1, 5]
def solution(citations):
    citations.sort(reverse=True) # [6,5,3,1,0]
    answer = max(map(min, enumerate(citations, start=1)))
    # [1, 6] ,[2,5],[3,3],[4,1],[5,0]
    return answer