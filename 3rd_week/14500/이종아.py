import sys

input = sys.stdin.readline

block1 = [[[1, 1, 1, 1]], [[1], [1], [1], [1]]]
block2 = [[[1, 1], [1, 1]]]
block3 = [
    [[1, 0], [1, 0], [1, 1]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1], [0, 1], [0, 1]],
    [[0, 0, 1], [1, 1, 1]],
    [[0, 1], [0, 1], [1, 1]],
    [[1, 0, 0], [1, 1, 1]],
    [[1, 1], [1, 0], [1, 0]],
    [[1, 1, 1], [0, 0, 1]],
]
block4 = [
    [[1, 0], [1, 1], [0, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[0, 1], [1, 1], [1, 0]],
    [[1, 1, 0], [0, 1, 1]],
]
block5 = [
    [[1, 1, 1], [0, 1, 0]],
    [[0, 1], [1, 1], [0, 1]],
    [[0, 1, 0], [1, 1, 1]],
    [[1, 0], [1, 1], [1, 0]],
]

blocks = block1 + block2 + block3 + block4 + block5


def _14500():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    for h in range(N):
        for w in range(M):
            for block in blocks:
                value = 0
                if h + len(block) <= N and w + len(block[0]) <= M:
                    for b_h in range(len(block)):
                        for b_w in range(len(block[b_h])):
                            if block[b_h][b_w] == 1:
                                value += board[h + b_h][w + b_w]
                answer = max(answer, value)
    print(answer)


if __name__ == "__main__":
    _14500()
