"""
N : 카드 수 // M : 네오가 가진 돈
팀 11명 구성 >>
GK 1명 
DF 3~5명
MF 2~5명
FW 1~4명
같은 선수 여러번 X

두 가지 종류의 비용 >>
스카웃 비용
선수 급여 비용

스카웃 비용의 합은 M을 초과하면 안된다.
선수 급여 비용 또한 120을 초과하면 안된다.

번호 : id // 포지션 : pos // 오버롤 : over // 가격 : cost // 급여 : salary // 이름 : name
"""
N, M = map(int, input().split())
id,pos,over,cost,salary,name = [],[],[],[],[],[]
for i in range(N):
    id[i],pos[i],over[i],cost[i],salary[i],name[i] = map(str,input().split())
    