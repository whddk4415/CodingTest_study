def _1912():
    N = int(input())
    numbers = [0] + list(map(int, input().split()))
    dp = [0] * (N+1)
    for i in range(1, N+1):
        dp[i] = max(dp[i-1] + numbers[i], numbers[i])
    print(max(dp[1:]))

if __name__ == '__main__':
    _1912()