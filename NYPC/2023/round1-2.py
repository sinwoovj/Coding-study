"""
문장 분석
1.
-리스트의 한 스트링이 M 값보다 넘어서면 문장을 두개로 분리함


한문장 씩 봄
그리고 바로 출력함

"""
def Normal(st):
    if len(st) > M:
        arr = list(map(str,st.split()))
        for i in range(len(arr)):
            print(arr[i]+("_"*(M-len(arr[i]))))
    elif len(st) <= M:
        print(st.replace(" ","_")+("_"*(M-len(st))))
def Center(st):
    if len(st) > M:
        arr = list(map(str,st.split()))
        for i in range(len(arr)):
            if(M-len(arr[i])%2==0):
                print(("_"*((M-len(arr[i]))/2))+arr[i]+("_"*((M-len(arr[i]))/2)))
            else:
                print(("_"*((M-len(arr[i]))//2))+arr[i]+("_"*((M-len(arr[i]))//2+1)))
    elif len(st) <= M:
        if(M-len(st)%2==0):
            print(("_"*((M-len(st))/2))+st.replace(" ","_")+("_"*((M-len(st))/2)))
        else:
            print(("_"*((M-len(st))//2))+st.replace(" ","_")+("_"*((M-len(st))//2+1)))
def Right(st):
    if len(st) > M:
        arr = list(map(str,st.split()))
        for i in range(len(arr)):
            print(("_"*(M-len(arr[i])))+arr[i])
    elif len(st) <= M:
        print(("_"*(M-len(st)))+st.replace(" ","_"))
book = []
cen,rig = False,False
N, M = map(int, input().split())
for _ in range(N):
    book.append(input())

for i in range(N):
    if(book[i] == "</CENTER>"):cen=False
    elif(book[i] == "</RIGHT>"):rig=False
    elif(book[i] == "<CENTER>"):cen=True
    elif(book[i] == "<RIGHT>"):rig=True
    elif(cen):Center(book[i])
    elif(rig):Right(book[i])
    else:Normal(book[i])