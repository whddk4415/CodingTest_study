const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `6 7 3
.......
...O...
....O..
.......
OO.....
OO.....
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [row, col, N] = input().split(" ");
let arr = [];

for (let i = 0; i < row; i++) {
  arr.push(input().split(""));
}

function solution() {
  const dx = [1, -1, 0, 0];
  const dy = [0, 0, 1, -1];

  // N이 설치 시점인 경우 바로 출력
  if (N % 2 === 0) {
    for (let i = 0; i < row; i++) {
      let temp = "";
      for (let j = 0; j < col; j++) {
        temp += "O";
      }
      console.log(temp);
    }
    return;
  }

  // 동서남북 방향 폭발
  const bomb = (x, y) => {
    for (let k = 0; k < 4; k++) {
      let nx = x + dx[k];
      let ny = y + dy[k];
      if (nx > -1 && nx < row && ny > -1 && ny < col) {
        if (arr[nx][ny] !== "O") {
          arr[nx][ny] = ".";
        }
      }
    }
  };

  for (let time = 3; time <= N; time = time + 2) {
    // 폭발 전 폭발 될 수 있는 부분 처리
    for (let i = 0; i < row; i++) {
      for (let j = 0; j < col; j++) {
        if (arr[i][j] === ".") {
          arr[i][j] = "T";
        }
      }
    }
    // 폭발
    for (let i = 0; i < row; i++) {
      for (let j = 0; j < col; j++) {
        if (arr[i][j] === "O") {
          bomb(i, j);
        }
      }
    }
    // 폭발 후 자신의 폭탄 자리 폭발, 임시 처리했던 부분 폭탄으로 변화
    for (let i = 0; i < row; i++) {
      for (let j = 0; j < col; j++) {
        if (arr[i][j] === "O") {
          arr[i][j] = ".";
        }
        if (arr[i][j] === "T") {
          arr[i][j] = "O";
        }
      }
    }
  }

  // 출력
  for (let i = 0; i < row; i++) {
    let temp = "";
    for (let j = 0; j < col; j++) {
      temp += arr[i][j];
    }
    console.log(temp);
  }
}

solution();
