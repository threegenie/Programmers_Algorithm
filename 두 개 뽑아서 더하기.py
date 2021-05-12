from itertools import combinations

def solution(numbers):
    lists = list(combinations(numbers,2)) #n개 중 2개를 뽑는 경우의 수 
    answer = []
    for i in range(len(lists)):
        sum = lists[i][0]+lists[i][1]
        answer.append(sum)
    answer = list(sorted(set(answer)))
    return answer
