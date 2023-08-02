"""
입력 : 
N은 열고 행의 크기 M은 폭발 범위 그리고 모기의 위치에 따른 수의 지표
출력 : 
물풍선을 십자모양 또는 엑스 자 모양으로 터뜨렸을 때의 최댓값

모든 위치를 검사해봐야하니까, 그리고 2차원 배열이니까 이중 for문 사용

함수 2개 하나는 십자일 경우 두번째는 대각선일 경우의 모기 수 반환
비교 후 또 반환

결론적으로 return 할 최댓값 max가 필요
"""

"""
while 문으로
위치값을 1씩 추가하고 해당 위치의 값을 total에 더함
만약 값이 0 미만으로 내려가거나 N 초과라면 그때부터는 while문을 벗어남
위 아래 왼쪽 오른쪽
"""

MAX = 0
N, M = map(int, input().split())
vil = []

def Comparison(i, j):
    global MAX
    compa = max(Cross(i, j), X(i, j))
    if MAX <= compa:
        MAX = compa
    return MAX

def Cross(i, j):
    total = 0
    for a in range(i - M, i + M + 1):
        if a < 0 or a >= N or a == i:
            continue
        total += vil[a][j]
    for b in range(j - M, j + M + 1):
        if b < 0 or b >= N:
            continue
        total += vil[i][b]
    return total

def X(i, j):
    total = 0
    for a in range(i - M, i + M + 1):
        if a < 0 or a >= N or a == i:
            continue
        b = j + (i - a)
        if b < 0 or b >= N:
            continue
        total += vil[a][b]
    return total

for _ in range(N):
    row = list(map(int, input().split()))
    vil.append(row)

for i in range(N):
    for j in range(N):
        Comparison(i, j)

print(MAX)
