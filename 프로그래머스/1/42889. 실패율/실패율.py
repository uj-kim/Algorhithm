# n: 스테이지 개수
# stages에 n+1 이 있으면 -> 클리어 한 사용자
# 실패율 = 1~n인 사용자들 / n+1인 사용자들
#실패율이 높은 스테이지 desc => answer
from collections import Counter

def solution(N, stages):
    cnt_stages = Counter(stages)
    participant = len(stages)
    answer = []
    real_answer = []
    
    for i in range(1, N+1):
        failure =  cnt_stages[i]
        
        if participant == 0:
            f_rate = 0
        else:
            f_rate = failure / participant
        
        answer.append((i, f_rate))
        participant -= failure
        
    answer.sort(key=lambda x: (-x[1], x[0]))
        
    for j in answer:
        a, b = j
        real_answer.append(a)
    return(real_answer)
        