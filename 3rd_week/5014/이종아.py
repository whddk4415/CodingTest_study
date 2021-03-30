from collections import deque

def _5014():
    F, S, G, U, D = map(int, input().split())
    queue = deque([S])
    visited = [float("inf") for _ in range(F + 1)]
    visited[S] = 0
    while queue:
        position = queue.popleft()
        if position == G:
            print(visited[G])
            return
        if position + U <= F and visited[position + U] > visited[position] + 1:
            visited[position + U] = visited[position] + 1
            queue.append(position + U)
        if position - D > 0 and visited[position - D] > visited[position] + 1:
            visited[position - D] = visited[position] + 1
            queue.append(position - D)
    print("use the stairs")


if __name__ == "__main__":
    _5014()