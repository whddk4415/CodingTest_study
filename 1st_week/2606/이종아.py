import sys
input = sys.stdin.readline

from collections import deque
def _2606():
    C = int(input())
    computer = [[] for _ in range(C+1)]
    for _ in range(int(input())):
        a, b = map(int, input().split())
        computer[a].append(b)
        computer[b].append(a)
    queue = deque(computer[1])
    visited = [False for _ in range(C+1)]
    visited[1] = True
    count = 0
    while queue:
        c = queue.popleft()
        if not visited[c]:
            count += 1
            queue.extend(computer[c])
            visited[c] = True
    return count

if __name__ == '__main__':
    print(_2606())
