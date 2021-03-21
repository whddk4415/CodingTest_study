const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `4 6
101111
101010
101011
111011
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [row, col] = input().split(" ");
let arr = [];

for (let i = 0; i < row; i++) {
  arr.push(input().split(""));
}
arr = arr.map((ele) => ele.map(Number));
function solution() {
  const queue = [];
  let dx = [1, 0, -1, 0];
  let dy = [0, 1, 0, -1];
  const isVisited = new Array(parseInt(row))
    .fill()
    .map((ele) => new Array(parseInt(col)).fill(false));
  queue.push([0, 0]);
  isVisited[0][0] = true;
  // bfs
  while (queue.length) {
    let [x, y] = queue.shift();
    for (let i = 0; i < 4; i++) {
      let nx = x + dx[i];
      let ny = y + dy[i];
      if (nx > -1 && nx < row && ny > -1 && ny < col) {
        if (!isVisited[nx][ny] && arr[nx][ny]) {
          queue.push([nx, ny]);
          arr[nx][ny] = arr[x][y] + 1;
          isVisited[nx][ny] = true;
        }
      }
    }
  }
  console.log(arr[row - 1][col - 1]);
}

solution();
