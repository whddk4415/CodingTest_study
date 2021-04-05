const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `3
2 2 1
1 0 1 0
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = input();
const numArr = input().split(" ").map(Number);
const operator = [];
input()
  .split(" ")
  .forEach((ele, idx) => {
    for (let i = 0; i < parseInt(ele); i++) {
      operator.push(idx);
    }
  });

function solution() {
  let max = -1000000001;
  let min = 1000000001;
  const isVisited = Array.from({ length: N - 1 }, (ele) => false);

  const dfs = (v, idx, num, len) => {
    let result = 0;
    if (len === N - 1) {
      if (num > max) {
        max = num;
      }
      if (num < min) {
        min = num;
      }
    } else {
      for (let i = 0; i < N - 1; i++) {
        if (!isVisited[i]) {
          if (operator[i] === 0) {
            result = num + numArr[idx];
          } else if (operator[i] === 1) {
            result = num - numArr[idx];
          } else if (operator[i] === 2) {
            result = num * numArr[idx];
          } else if (operator[i] === 3) {
            result = parseInt(num / numArr[idx]);
          }
          isVisited[i] = true;
          dfs(i, idx + 1, result, len + 1);
        }
      }
    }
    isVisited[v] = false;
  };
  dfs(0, 1, numArr[0], 0);
  console.log(parseInt(max));
  console.log(parseInt(min));
}

solution();
