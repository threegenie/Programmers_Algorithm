#수포자 모의고사 문제 - 수학문제를 전부 찍는 3인

def solution(answers):
    student1 = [1,2,3,4,5] 
    student2 = [2,1,2,3,2,4,2,5] 
    student3 = [3,3,1,1,2,2,4,4,5,5] 
    answer = []
    scores = [0,0,0] 

    for i in range(len(answers)):
        if answers[i] == student1[i%len(student1)]:
            scores[0] += 1
        if answers[i] == student1[i%len(student2)]:
            scores[1] += 1
        if answers[i] == student1[i%len(student3)]:
            scores[2] += 1
        
    for i in range(3):
        if scores[i] == max(scores):
           answer.append(i+1)

    return answer


'''
수포자 모의고사 문제를 풀었습니다. 학생들이 문제를 찍는 패턴을 각각 배열에 저장해주고, 입력받은 정답을 학생들의 답안 패턴으로 나눠 학생들의 답안 패턴과 같다면 점수를 올리는 식으로, 다소 직관적으로 문제를 해결했습니다.
'''
