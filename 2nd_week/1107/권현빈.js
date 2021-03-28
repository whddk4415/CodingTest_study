const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `99
  1
  8 
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = parseInt(input());
const brokenNum = parseInt(input());
let brokenArr = [];

brokenArr = input().split(" ").slice();

function solution() {
  let time = 0;
  let answer = [];
  if (N == 100) {
    console.log(0);
    return;
  }
  let isFinish = true;
  let check = String(N).split("");

  for (let i = 0; i < check.length; i++) {
    if (brokenArr.indexOf(check[i]) !== -1) {
      isFinish = false;
    }
  }
  if (isFinish) {
    console.log(Math.min(check.length, Math.abs(N - 100)));
    return;
  }

  while (time < 500000) {
    time++;
    const over = String(N + time).split("");
    const lower = String(Math.max(N - time, 0)).split("");
    let isFinishL = true;
    let isFinishO = true;
    for (let i = 0; i < lower.length; i++) {
      if (brokenArr.indexOf(lower[i]) !== -1) {
        isFinishL = false;
      }
    }
    if (isFinishL) {
      answer.push(time + lower.length);
    }

    for (let i = 0; i < over.length; i++) {
      if (brokenArr.indexOf(over[i]) !== -1) {
        isFinishO = false;
      }
    }

    if (isFinishO) {
      answer.push(time + over.length);
    }

    if (isFinishL || isFinishO) {
      answer.push(Math.abs(N - 100));
      console.log(Math.min(...answer));
      return;
    }
  }
  console.log(Math.abs(N - 100));
}

solution();
