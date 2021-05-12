from itertools import combinations
def solution(numbers):
    lists = list(combinations(numbers,2))
    i=0
    answer=[]
    for i in range(len(lists)):
        sum = lists[i][0]+lists[i][1]
        answer.append(sum)
    answer = list(set(sorted(answer)))
    return answer
