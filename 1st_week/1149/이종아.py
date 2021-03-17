import sys
input = sys.stdin.readline

def _1149():
    N=int(input())
    streets=[list(map(int, input().split())) for _ in range(N)]
    for i in range(1, len(streets)):
        for j in range(len(streets[i])):
            streets[i][j] = streets[i][j] + min([v for idx, v in enumerate(streets[i-1]) if idx != j])
    print(min(streets[-1]))


if __name__ == '__main__':
    _1149()