def solution(phone_number):
    # length = len(phone_number)
    # star = (length-4)*'*'
    # num = phone_number[-4:]
    # answer = star+num
    # return answer
    
    return (len(phone_number)-4)*'*'+phone_number[-4:] #한줄로 끝내기!

    
