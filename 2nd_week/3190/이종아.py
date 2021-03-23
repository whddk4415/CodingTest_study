import sys
input = sys.stdin.readline
from collections import deque

def change_direction(direction, command):
    if command == 'D':
        if direction[0] != 0:
            new_direction = (direction[1], direction[0])
        elif direction[1] != 0:
            new_direction = (-direction[1], -direction[0])
    else:
        if direction[0] != 0:
            new_direction = (-direction[1], -direction[0])
        elif direction[1] != 0:
            new_direction = (direction[1], direction[0])
    return new_direction

def _3190():
    N, K = int(input()), int(input())
    board = [[0 for _ in range(N)] for _ in range(N)]
    for _ in range(K):
        y, x = map(int, input().split())
        board[y-1][x-1] = 1

    L = int(input())
    moves = deque([tuple(input().rstrip().split()) for _ in range(L)])
    direction = (1, 0)
    head = (0, 0)
    snakes = deque([(0, 0)])
    time = 0
    while 0 <= head[0] < N and 0 <= head[1] < N:
        if moves and int(moves[0][0]) == time:
            direction = change_direction(direction, moves.popleft()[1])
        head = (head[0] + direction[0], head[1] + direction[1])
        time += 1
        if head[0] < 0 or head[0] >= N or head[1] < 0 or head[1] >= N:
            print(time)
            return
        if head in snakes:
            print(time)
            return
        if board[head[1]][head[0]] == 0:
            snakes.popleft()
        else:
            board[head[1]][head[0]] = 0
        snakes.append(head)

    print(time)

if __name__ == '__main__':
    _3190()
