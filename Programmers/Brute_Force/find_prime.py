from itertools import permutations
import math


def solution(string):

    # 소수 set
    string_multi_set = list(string)
    s_space = []

    # 해 공간 generate
    for length in range(len(string)):
        permu = permutations(string_multi_set, length + 1)
        for n in permu:
            n = "".join(n)
            num = int(n)
            if num in s_space:
                continue
            s_space.append(num)

    # 소수 탐색 알고리즘
    cnt = 0
    for candidate in s_space:
        flag = True
        upper_bound = int(math.sqrt(candidate))

        if candidate == 0 or candidate == 1:
            continue

        for i in range(2, upper_bound + 1):
            if candidate % i == 0:
                flag = False

        if flag:
            cnt += 1

    return cnt


string = "1101"

prime_cnt = solution(string)
print(prime_cnt)
