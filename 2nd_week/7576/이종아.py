import sys
input = sys.stdin.readline
from collections import deque
def _7576():
    M, N = map(int, input().split())
    box, tomatoes = [], deque()
    for r in range(N):
        row = list(map(int, input().split()))
        for c in range(M):
            if row[c] == 1:
                tomatoes.append((c, r))
        box.append(row)
    answer = -1
    while tomatoes:
        answer += 1
        for _ in range(len(tomatoes)):
            x, y = tomatoes.popleft()
            for dx, dy in zip((1, -1, 0, 0), (0, 0, 1, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < M and 0 <= ny < N and box[ny][nx] == 0:
                    box[ny][nx] = 1
                    tomatoes.append((nx, ny))
    print(answer if all([all(row) for row in box]) else -1)


if __name__ == '__main__':
    _7576()