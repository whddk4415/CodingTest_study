# url: https://www.acmicpc.net/problem/16918
# level: Silver 1
# Done!


def wait_and_bomb(bombs, R, C):
    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for r in range(R):
        for c in range(C):
            if bombs[r][c][0]:
                bombs[r][c][1] += 1
    for r in range(R):
        for c in range(C):
            if bombs[r][c][1] == 3:
                bombs[r][c] = [False, 0]
                for dc, dr in dxy:
                    if (
                        0 <= r + dr < R
                        and 0 <= c + dc < C
                        and bombs[r + dr][c + dc][1] != 3
                    ):
                        bombs[r + dr][c + dc] = [False, 0]
    return bombs


def put_bomb_to_blank(bombs, R, C):
    for r in range(R):
        for c in range(C):
            if bombs[r][c][0]:
                bombs[r][c][1] += 1
            else:
                bombs[r][c][0] = True
    return bombs


def _16918():
    R, C, N = map(int, input().split())
    bombs = [[[False, 0] for _ in range(C)] for _ in range(R)]
    for r in range(R):
        row = list(input().rstrip())
        for c in range(C):
            if row[c] == "O":
                bombs[r][c][0] = True
    for i in range(1, N + 1):
        if i % 2 == 0:
            put_bomb_to_blank(bombs, R, C)
        else:
            wait_and_bomb(bombs, R, C)
    for r in range(R):
        for c in range(C):
            if bombs[r][c][0]:
                print("O", end="")
            else:
                print(".", end="")
        print()


if __name__ == "__main__":
    _16918()
