def solution(answers):
    #문제 찍는 패턴
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]
    
    #학생들 점수
    s1 = 0
    s2 = 0
    s3 = 0
    
    #return할 리스트
    score = []
    
    #정답과 찍는 패턴 배열 비교해서 점수 내기
    for i in range(len(answers)):
        if answers[i]==student1[i%5]:
            s1+=1
        if answers[i]==student2[i%8]:
            s2+=1
        if answers[i]==student3[i%10]:
            s3+=1
    
    max_score = max(s1,s2,s3) #점수 가장 높은 사람 찾기
    
    #점수가 가장 높으면 배열에 넣어서 return
    if max_score == s1
        score.append(1)
    if max_score == s2:
        score.append(2)
    if max_score == s3:
        score.append(3)
    
    return score
        
        
    
