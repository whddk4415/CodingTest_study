import sys

input = sys.stdin.readline


def solution():
    N, K = map(int, input().split())
    coins = []
    for _ in range(N):
        coins.append(int(input()))
    sum = 0
    ans = 0
    for coin in reversed(coins):
        ans += K // coin
        K = K % coin
        if(K == 0):
            print(ans)
            return


solution()
