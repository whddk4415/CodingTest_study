const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `6 6 16
0 0 0 0 1 1
0 0 0 0 0 2
1 1 1 0 1 0
0 0 0 0 0 0
0 1 1 1 1 1
0 0 0 0 0 0
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, M, T] = input().split(" ");
const arr = [];

for (let i = 0; i < N; i++) {
  arr.push(input().split(" "));
}
arr[N - 1][M - 1] = "F";

function solution() {
  let dx = [1, 0, -1, 0];
  let dy = [0, 1, 0, -1];
  const timeArr = [];
  const getArr = [];
  const queue = [];
  const isVisited = new Array(2)
    .fill()
    .map(() =>
      new Array(parseInt(N))
        .fill()
        .map(() => new Array(parseInt(M)).fill(false))
    );

  queue.push([0, 0]);
  timeArr.push(0);
  getArr.push(false);
  isVisited[0][0][0] = true;
  isVisited[1][0][0] = true;
  //bfs
  while (queue.length) {
    let [x, y] = queue.shift();
    let time = timeArr.shift();
    let get = getArr.shift();
    for (let dir = 0; dir < 4; dir++) {
      let nx = x + dx[dir];
      let ny = y + dy[dir];
      if (nx >= 0 && nx < N && ny >= 0 && ny < M) {
        // get = false
        if (!get) {
          if (!isVisited[0][nx][ny] && arr[nx][ny] != 1) {
            queue.push([nx, ny]);
            timeArr.push(time + 1);
            isVisited[0][nx][ny] = true;
            if (arr[nx][ny] == 2) {
              getArr.push(true);
            } else {
              getArr.push(false);
            }
          }
        } else {
          if (!isVisited[1][nx][ny]) {
            queue.push([nx, ny]);
            timeArr.push(time + 1);
            isVisited[1][nx][ny] = true;
            getArr.push(true);
          }
        }
        if (arr[nx][ny] === "F") {
          console.log(time + 1);
          return;
        }
        if (time + 1 > T) {
          console.log("Fail");
          return;
        }
      }
    }
  }
  console.log("Fail");
}

solution();
