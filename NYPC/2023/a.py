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
GK 1명 DF 3명 MF 2명 FW 1명을 먼저 골라서 최소를 맞추는데 일단은 가장 정렬 상
높은 순위대로 뽑고 했다가 안되면
GK를 제외한 나머지 추가 모집 가능 인원인 DF 2명, MF 3명, FW 3명을 뽑아야한다.
그러기 위해서는 GK를 제외한 DF,MF,FW 리스트 세 개를 합치고 정렬한 후
DF,MF,FW 중에서 추가적으로 고름 (DF는 2명만 더 가능, 나머지는 3명)
이후 정렬된 팀 후보를 차례대로 비용 

만약 기존 팀에 최적화를 위한 선수를 투입했을 때 규율에 어긋나는지 테스트하고
된다면 기존 팀에 추가하고 안된다면 다음 선수
for문을 돌때마다 DF나 MF,FW의 정원이 찼다면 바로 pos가 정원이 다찬 딕셔너리는
optm에서 삭제한다.
"""
# 같은 선수 중복 제거(최적 조건)
def custom_sort(item):
    return (-int(item["over"]), int(item["cost"]), int(item["salary"]))
# 규제 테스트
def test(lst):
    total_cost = sum(int(dct["cost"]) for dct in lst)
    total_salary = sum(int(dct["salary"]) for dct in lst)
    if total_cost <= M and total_salary <= 120:
        return sum(int(dct["over"]) for dct in lst)
    else:
        return 1
# 겹치는 선수 삭제 함수
def remove_duplicate_dict(lst, a):
    indexes_to_remove = []

    for i, dct in enumerate(lst):
        if dct == a:
            indexes_to_remove.append(i)

    for index in reversed(indexes_to_remove):
        lst.pop(index)
# 추가적으로 오버롤 올릴 수 있는 최적의 팀 만들기
def operate_team(dtm, optm):
    gk,df,mf,fw=1,5,5,4
    for pl in optm:
        dtm.append(pl)
        if test(dtm) == 1:
            dtm.remove(pl)
        else:
            if pl["pos"] == "GK": gk-=1
            elif pl["pos"] == "DF": df-=1
            elif pl["pos"] == "MF": mf-=1
            elif pl["pos"] == "FW": fw-=1
        if gk == 0: optm = [d for d in optm if d["pos"] != "GK"]
        elif df == 0: optm = [d for d in optm if d["pos"] != "DF"]
        elif mf == 0: optm = [d for d in optm if d["pos"] != "MF"]
        elif fw == 0: optm = [d for d in optm if d["pos"] != "FW"]
    for i in dtm: print(i)
    return test(dtm)

# 최소 규격 팀 만들기
def make_team(gk,df,mf,fw):
    for a in range(len(gk)):
        for b in range(len(df)-2):
            for c in range(len(mf)-1):
                for d in range(len(fw)):
                    tm = [gk[a],df[b],df[b+1],df[b+2],mf[c],mf[c+1],fw[d]]
                    res = test(tm)
                    if res == 1:
                        continue
                    else:
                        optm = df+mf+fw
                        for _ in range(1,len(tm)):
                            remove_duplicate_dict(optm,tm[_])
                        optm.sort(key=custom_sort)
                        return operate_team(tm,optm)
    return -1
# 입력
N, M = map(int, input().split())
player = {}
pos,over,cost,salary,name = ['']*N,[0]*N,[0]*N,[0]*N,['']*N
for i in range(N):
    pos[i],over[i],cost[i],salary[i],name[i] = map(str,input().split())
for i in range(N):
    player[i] = {
        "id": i,
        "pos": pos[i],
        "over": over[i],
        "cost": cost[i],
        "salary": salary[i],
        "name": name[i],
    }
# "name" 키의 값이 중복되는 딕셔너리들 중 가장 위에 있는 딕셔너리를 제외하고 삭제
unique_names = set()
sorted_unique_data = []
for i in range(N):
    if (player[i])["name"] not in unique_names:
        sorted_unique_data.append(player[i])
        unique_names.add((player[i])["name"])
# over, cost, salary 기준으로 정렬
sorted_unique_data.sort(key=custom_sort)
# print(sorted_unique_data)
# 포지션 별 분리
GK,DF,MF,FW = [],[],[],[]
for player in sorted_unique_data:
    if player["pos"] == "GK":
        GK.append(player)
    elif player["pos"] == "DF":
        DF.append(player)
    elif player["pos"] == "MF":
        MF.append(player)
    elif player["pos"] == "FW":
        FW.append(player)
sorted_GK = sorted(GK, key=custom_sort)
sorted_DF = sorted(DF, key=custom_sort)
sorted_MF = sorted(MF, key=custom_sort)
sorted_FW = sorted(FW, key=custom_sort)
print(make_team(GK,DF,MF,FW))

"""
그냥 처음부터 입력만 받고
싹다 정렬하고
이름 같으면 삭제
각 포지션 별로 최소 인원만큼 뽑고
최대 인원 넘으면 해당 포지션인 딕셔너리 전체 삭제해가며 추가 인원 충당
{정렬조건
오버롤만 따질때
가격만, 또는 봉급만 따질때 비교해서 max 값 반환}
총 오버롤 반환 그리고 출력
"""