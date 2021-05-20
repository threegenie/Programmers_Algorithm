from math import gcd
def solution(n, m):
    answer = [0,0]
    gc = gcd(n,m)
    lc = n*m//gc
    answer[0] = gc
    answer[1] = lc
    return answer
    
        
    
