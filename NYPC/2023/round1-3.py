def min_operations(X, K):
    dp = [0] * (2 ** K)  # dp 배열 크기를 2^K로 수정
    for i in range(1, 2 ** K):
        option1 = (X + 1) % i
        option2 = (X * 2) % i
        dp[i] = min(dp[option1] + 1, dp[option2] + 1)
    return dp[2 ** K - 1]  # 결과는 dp[2^K - 1]에 저장됨

# 입력 받기
K = int(input())
X_binary = input()

# 이진수를 10진수로 변환
X = int(X_binary, 2)

# 최소 연산 횟수 계산
result = min_operations(X, K)

# 결과 출력
print(result)
