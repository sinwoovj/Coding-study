"""
문장 분석
1.
-리스트의 한 스트링이 M 값보다 넘어서면 문장을 두개로 분리함
한문장 씩 봄
그리고 바로 출력함

M 번째가 공백일 경우
M 이하의 문자열 이내에 2개 이상의 공백이 존재할 경우 for문으로 뒤에도 계속 검사
a+b >문자열 수 > M 아니 a = a+b => a+b 문자열수 >M 예 a resarr 추가 a+b는 원래 arr에서 pop 하고 처음부터
"""
def Newline(arr):
    exarr = arr
    resarr=[]
    a = exarr[0]
    for i in range(1,len(exarr)):
        if(len(a + '-' + exarr[i]) > M):
            resarr.append(a)
            a = exarr[i]
        else:
            a = a + '-' + exarr[i]
    if a:  # 마지막에 남은 문자열 추가
        resarr.append(a)
    return resarr
def Normal(st):
    if len(st) > M:
        arr = Newline(list(map(str,st.split('-'))))
        for i in range(len(arr)):
            print(("-"*(M-len(arr[i])))+arr[i]) if rig else print(arr[i]+("-"*(M-len(arr[i]))))
    else:
        print(st+("-"*(M-len(st)))) if rig else print(("-"*(M-len(st)))+st)
def Center(st):
    if len(st) > M:
        arr = Newline(list(map(str,st.split('-'))))
        for i in range(len(arr)):
            padding = (M - len(arr[i])) // 2
            print(("-" * padding) + arr[i] + ("-" * (padding + (M - len(arr[i])) % 2)))
    else:
        padding = (M - len(st)) // 2
        print(("-" * padding) + st + ("-" * (padding + (M - len(st)) % 2)))
            
book = []
cen,rig = False,False
N, M = map(int, input().split())
for _ in range(N):
    book.append(input())
# 리스트 컴프리헨션을 통해 공백을 '-'으로 치환
book = [s.replace(' ', '-') for s in book]
for i in range(N):
    if(book[i] == "</CENTER>"):cen=False
    elif(book[i] == "</RIGHT>"):rig=False
    elif(book[i] == "<CENTER>"):cen=True
    elif(book[i] == "<RIGHT>"):rig=True
    elif(cen):Center(book[i])
    else:Normal(book[i])