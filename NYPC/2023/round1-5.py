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

1. 팀 11명 구성을 오버롤이 가장 높게 구성을 한 것을 a 리스트에 배열함
2. 비용 규칙을 검토하고 높은 것을 차례로 검사하다 적합된 것이 있으면 해당 팀의 오버롤을 출력하고 끝
각 포지션으로 나누고 오버롤 대로 정렬시킴.
GK 1명 DF 3명 MF 2명 FW 1명을 먼저 골라서 최소를 맞추고,
DF,MF,FW 중에서 추가적으로 고름 (DF는 2명만 더 가능, 나머지는 3명)
이후 정렬된 팀 후보를 차례대로 비용 
"""
N, M = map(int, input().split())
player = {}
pos,over,cost,salary,name = ['']*N,[0]*N,[0]*N,[0]*N,['']*N
for i in range(N):
    pos[i],over[i],cost[i],salary[i],name[i] = map(str,input().split())
for i in range(N):
    player[i] = {
        "pos": pos[i],
        "over": over[i],
        "cost": cost[i],
        "salary": salary[i],
        "name": name[i],
    }
