def solution(a, b, n):
    
    # 구하려는 것 : 상빈이가 받을 수 있는 콜라의 병 수
    answer = 0
    
    #콜라 병(n)이 교환할 수 있는 병(a)보다 적게 남으면 종료
    while n >= a:
        #교환할 수 있는 병의 개수
        e = n // a
        # 새로 받은 병의 개수
        nb = b * e
        # answer 갱신
        answer += nb
        # 남은 병 개수 갱신 : 교환 후 남은 병 + 새로 받은 병
        n = n % a + nb
    
    return answer
        