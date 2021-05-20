def solution(n):
    answer = []
    n = str(n)
    reverse = n[::-1]
    i = 0
    for i in range(len(reverse)):
        answer.append(int(reverse[i]))
    return answer
