import sys

input = sys.stdin.readline
from collections import deque


def bfs(start, graph):
    m = s = 0
    queue = deque()
    visited = [False for _ in range(len(graph) + 1)]
    visited[start[0]] = True
    queue.append(start)
    trace = set()
    while queue:
        v, cumulative_value = queue.popleft()
        trace.add(v)
        for e, value in graph[v].items():
            if not visited[e]:
                visited[e] = True
                queue.append((e, value + cumulative_value))
                if value + cumulative_value > s:
                    s = cumulative_value + value
                    m = e

    return m, s, trace


def _1167():
    V = int(input())
    graph = {i: {} for i in range(1, V + 1)}
    index_set = set(range(1, V + 1))
    result = 0
    for _ in range(V):
        v, *info = map(int, input().split())
        for i in range(0, len(info) - 1, 2):
            des, value = info[i], info[i + 1]
            graph[v][des] = value
    while index_set:
        start = index_set.pop()
        _, value, trace = bfs((bfs((start, 0), graph)[0], 0), graph)
        result = max(result, value)
        index_set -= trace
    print(result)


if __name__ == "__main__":
    _1167()
