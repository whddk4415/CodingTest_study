const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [M, N] = input().split(" ").map(Number);
const tomatoMap = [];

for (let i = 0; i < N; i++) {
  tomatoMap.push(input().split(" "));
}

function solution() {
  let dx = [1, 0, -1, 0];
  let dy = [0, 1, 0, -1];
  const queue = [];
  let answer = 0;

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (tomatoMap[i][j] == 1) {
        queue.push([i, j, 0]);
      }
    }
  }

  while (queue.length > 0) {
    let [x, y, day] = queue.shift();
    answer = day;
    for (let dir = 0; dir < 4; dir++) {
      let nx = x + dx[dir];
      let ny = y + dy[dir];
      if (nx < N && nx >= 0 && ny < M && ny >= 0) {
        if (tomatoMap[nx][ny] == 0) {
          queue.push([nx, ny, day + 1]);
          tomatoMap[nx][ny] = 1;
        }
      }
    }
  }

  console.log(answer);
}

solution();
