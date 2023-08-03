def min_operations(X, K):
    dp = [float('inf')] * (2 ** K)
    dp[X] = 0

    for i in range(X, 0, -1):
        next_i = (i + 1) % (2 ** K)
        double_i = (i * 2) % (2 ** K)
        
        dp[i] = min(dp[i], dp[next_i] + 1, dp[double_i] + 1)

    return dp[X]

# 입력 받기
K = int(input())
X_binary = input()

# 이진수를 10진수로 변환
X = int(X_binary, 2)

# 최소 연산 횟수 계산
result = min_operations(X, K)

# 결과 출력
print(result)
