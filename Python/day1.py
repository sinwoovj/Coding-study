"""

https://www.acmicpc.net/problem/13545

< 수열과 쿼리 0 >

1과 -1로만 이루어져 있는 길이가 N인 수열 A1, A2, ..., AN이 주어진다. 이때, 다음 쿼리를 수행하는 프로그램을 작성하시오.

i j: Ai, Ai+1, ..., Aj로 이루어진 부분 수열 중에서 합이 0이면서 가장 긴 연속하는 부분 수열의 길이를 출력한다.

"""
N = int(input())
A = list(map(int, input().split()))
M = int(input())
for a in range(M):
    k = list(map(int, input().split))
    j = k[0]
    dif = k[1] - k[0]
    p_cnt = 0
    m_cnt = 0
    for b in range(dif):
        if A[j] == 1: p_cnt += 1
        elif A[j] == -1: m_cnt += 1
        j+=1
    p_cnt

