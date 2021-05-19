def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i]%divisor==0:
            answer.append(arr[i])
    if answer==[]: #나누어떨어지는 원소가 없어서 배열이 비어있을 경우
        answer.append(-1)
    answer.sort()
    
    return answer
