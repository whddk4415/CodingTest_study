const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const boardSize = parseInt(input());
const appleNum = parseInt(input());
const appleMap = new Array(parseInt(boardSize))
  .fill()
  .map((ele) => new Array(parseInt(boardSize)).fill(false));
for (let i = 0; i < appleNum; i++) {
  let [x, y] = input().split(" ").map(Number);
  appleMap[x - 1][y - 1] = true;
}
const dirNum = input();
const dirData = [];
for (let i = 0; i < dirNum; i++) {
  dirData.push(input().split(" "));
}

function solution() {
  let time = -1;
  const snake = [[0, 0]];
  const dx = [0, 1, 0, -1]; // 우, 하, 좌, 상
  const dy = [1, 0, -1, 0]; // 우, 하, 좌, 상
  let dir = dirData.shift();
  let dirNum = 0; // 우
  while (true) {
    const headPos = snake[0].slice();
    time++;

    if (dir[0] == time) {
      if (dir[1] === "D") {
        dirNum = (dirNum + 1) % 4;
      } else {
        dirNum = (dirNum - 1 + 4) % 4;
      }
      if (dirData.length) {
        dir = dirData.shift();
      }
    }
    let nx = headPos[0] + dx[dirNum];
    let ny = headPos[1] + dy[dirNum];

    if (nx < 0 || nx >= boardSize || ny < 0 || ny >= boardSize) {
      console.log(time + 1);
      return;
    }
    //일단늘리는 뱀이라 여기서 체크해야함
    for (let i = 0; i < snake.length; i++) {
      if (snake[i][0] === nx && snake[i][1] === ny) {
        console.log(time + 1);
        return;
      }
    }
    if (appleMap[nx][ny]) {
      snake.unshift([nx, ny]);
      appleMap[nx][ny] = false;
    } else {
      snake.pop();
      snake.unshift([nx, ny]);
    }
  }
}

solution();
