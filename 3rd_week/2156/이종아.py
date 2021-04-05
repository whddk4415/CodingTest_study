import sys

input = sys.stdin.readline


def _2156():
    wines = [int(input()) for _ in range(int(input()))]
    dp = [0, wines[0]]
    for i in range(1, len(wines)):
        if len(dp) < 3:
            dp.append(dp[-1] + wines[i])
        else:
            dp.append(
                max(max(dp[:i]) + wines[i], max(dp[: i - 1]) + wines[i - 1] + wines[i])
            )
        print(dp)
    print(max(dp))


if __name__ == "__main__":
    _2156()
