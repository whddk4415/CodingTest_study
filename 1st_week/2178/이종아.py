import sys
from collections import deque

input = sys.stdin.readline


def _2178():
    N, M = map(int, input().split())
    _map = [list(map(int, input().rstrip())) for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[0][0] = True
    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque([(0, 0, 1)])
    while queue:
        x, y, cnt = queue.popleft()
        if x == M - 1 and y == N - 1:
            print(cnt)
            return
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if (
                (0 <= nx < M and 0 <= ny < N)
                and (not visited[ny][nx])
                and (_map[ny][nx] == 1)
            ):
                visited[ny][nx] = True
                queue.append((nx, ny, cnt + 1))


if __name__ == "__main__":
    _2178()