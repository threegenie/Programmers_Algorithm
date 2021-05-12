def solution(array, commands):
    answer = []
    for i in commands:
        arr = array[i[0]-1:i[1]] #자르고
        arr.sort() #정렬
        answer.append((arr[i[2]-1])) #k번째 수 넣기
    return answer
