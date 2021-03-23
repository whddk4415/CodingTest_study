N, M, T = map(int, input().split())
background = []
sord = 10000000
answer = 10000000
result = 10000000

move_x = [1, 0, -1, 0]
move_y = [0, -1, 0, 1]

for i in range(N):
    background.append(list(map(int, input().split())))

count = [[0] * M for _ in range(N)]
will_visit = []

will_visit.append((0, 0))

while (will_visit):
    x, y = will_visit.pop(0)

    if background[x][y] == 2:
        sord = count[x][y] + (M - 1 - x) + (N - 1 - y)

    if x == N - 1 and y == M - 1:
        result = count[x][y]
        break

    else:
        for i in range(4):
            nx = x + move_x[i]
            ny = y + move_y[i]

            if nx < 0 or ny < 0 or nx > N - 1 or ny > M - 1 or background[nx][ny] == 1:
                continue

            else:
                if count[nx][ny] == 0:
                    will_visit.append((nx, ny))
                    count[nx][ny] = count[x][y] + 1

answer = min(sord, result)
if answer <= T:
    print(answer)

else:
    print("Fail")
