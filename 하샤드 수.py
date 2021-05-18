def solution(x):
    a = []
    b = 0
    for i in str(x):
        a.append(i)
        b += int(i)
    
    if x%b==0:
        return True
    else:
        return False
