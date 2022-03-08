import math

# -*- coding: utf-8 -*-

def primenumber1(x):
    for i in range (2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
        return True

print(primenumber1(7))



# def primenumber(x):
#     for i in range(2,x):
#         if x % i == 0:
#             return False
#         return  True