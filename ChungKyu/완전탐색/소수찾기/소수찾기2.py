import itertools

# -*- coding: utf-8 -*-
def solution (numbers):
    prime_set= set()

    # 1. 모든 숫자 조합을 만든다.
    for i in range (len(numbers)):
        # print(list(numbers))
        numbers_permutation = itertools.permutations(list(numbers), i + 1)
        # print(list(numbers_permutation))
        # print(list(map("".join,numbers_permutation)))
        # print(list(map(int,map("".join,numbers_permutation))))
        numbers_perm_list = map(int,map("".join,numbers_permutation))
        prime_set |= set(numbers_perm_list)

    # print(prime_set)
    # 2. 소수가 아닌 수를 제외한다.
    prime_set -= set(range(0,2))
    lim = int(max(prime_set) ** 0.5) + 1
    print(lim)
    for i in range(2, lim):
        prime_set -= set(range(i*2, max(prime_set)+1, i))
    return len(prime_set)


print(solution("17"))