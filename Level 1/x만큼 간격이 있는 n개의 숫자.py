def solution(x, n):
    answer = []
    ran = x*n
    if x>0:
        for i in range(x,ran+1,x):
            answer.append(i)
    else:
        for i in range(x,ran-1,x):
            answer.append(i)
    return answer
        

# 테스트 8 런타임 에러로 통과 못함.. 정확도 92.9
# 왜 안되는거지?
