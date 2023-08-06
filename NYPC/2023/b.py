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
    if a:
        resarr.append(a)
    return resarr
book = []
cen,rig = False,False
N, M = map(int, input().split())
for _ in range(N):
    book.append(input())
book = [s.replace(' ', '-') for s in book]
for i in range(N):
    if(book[i] == "</CENTER>"):cen=False
    elif(book[i] == "</RIGHT>"):rig=False
    elif(book[i] == "<CENTER>"):cen=True
    elif(book[i] == "<RIGHT>"):rig=True
    elif(cen):
        if len(book[i]) > M:
            arr = Newline(list(map(str,book[i].split('-'))))
            for i in range(len(arr)):
                padding = (M - len(arr[i])) // 2
                print(("-" * padding) + arr[i] + ("-" * (padding + (M - len(arr[i])) % 2)))
        else:
            padding = (M - len(book[i])) // 2
            print(("-" * padding) + book[i] + ("-" * (padding + (M - len(book[i])) % 2)))
    else:
        if len(book[i]) > M:
            arr = Newline(list(map(str,book[i].split('-'))))
            for i in range(len(arr)):
                print(("-"*(M-len(arr[i])))+arr[i]) if rig else print(arr[i]+("-"*(M-len(arr[i]))))
        else:
            print(book[i]+("-"*(M-len(book[i])))) if not rig else print(("-"*(M-len(book[i])))+book[i])