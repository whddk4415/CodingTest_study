import sys
from collections import deque

input = sys.stdin.readline
def _17836():
    N, M, T = map(int, input().split())
    _map = [list(map(int, input().split())) for _ in range(N)]
    dxy = ((1, 0), (-1, 0), (0, 1), (0, -1))
    visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(2)]
    visited[False][0][0] = True
    queue = deque([(0, 0, False)])
    time = 0
    while queue:
        if time > T:
            print("Fail")
            return
        for _ in range(len(queue)):
            x, y, has_geuram = queue.popleft()
            if x == M - 1 and y == N - 1:
                print(time)
                return
            if _map[y][x] == 2:
                has_geuram = True
            for dx, dy in dxy:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= M or ny < 0 or ny >= N:
                    continue
                if visited[has_geuram][ny][nx]:
                    continue
                if has_geuram or _map[ny][nx] != 1:
                    visited[has_geuram][ny][nx] = True
                    queue.append((nx, ny, has_geuram))
        time += 1
    print("Fail")


if __name__ == "__main__":
    _17836()
