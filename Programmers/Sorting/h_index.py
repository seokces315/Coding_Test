def solution(citations):

    # 정렬된 citations 얻기
    citations.sort()
    print(citations)
    cit_length = len(citations)

    # flag = True까지 돌기
    for c in citations:
        # position 찾기
        pos = citations.index(c)
        # Branch
        if cit_length - pos <= c:
            break

    return c


citations = [3, 0, 6, 1, 5]
c = solution(citations)
print(c)
