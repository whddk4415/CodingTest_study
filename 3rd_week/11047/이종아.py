import sys

input = sys.stdin.readline


def _11047():
    N, K = map(int, input().split())
    coins = [int(input()) for _ in range(N)]
    answer = 0
    for coin in sorted(coins, reverse=True):
        p, K = divmod(K, coin)
        answer += p
    print(answer)


if __name__ == "__main__":
    _11047()