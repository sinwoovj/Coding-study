"""
{문제}
N:몬스터 수 // M:용사의 수
S:몬스터 정수 // A:몬스터 체력
T:용사의 정수 // B:용사의 공격력
정수는 0일 경우 불의 속성, 1일 경우 얼음의 속성
같은 속성으로 공격 시 1/2, 다른 속성으로 공격 시 공격력 그대로
용사의 공격력이 홀수가 될 시 버림한다.
"""
"""
{로직}
적1 적2
용1 용2
가능할때 해당 적에 카운트 +1
"""
    
def fight(st,ed):
    dict = {}
    for i in range(N):
        dict[i] = 0 
    for a in range(N):
        for b in range(st,ed+1):
            atk = B[b]
            if(S[a]==T[b]):
                atk = atk//2
            if(A[a]<=atk):
                dict[a]+=1
            if 0 not in dict.values(): print(1,end="");return 0
    print(0,end="")
S,A,T,B = [0]*100000,[0]*100000,[0]*100000,[0]*100000
N, M = map(int, input().split())
for i in range(N):
    S[i],A[i] = map(int,input().split())
for i in range(M):
    T[i],B[i] = map(int,input().split())
for i in range(M-N+1):
    fight(i,i+N-1)
