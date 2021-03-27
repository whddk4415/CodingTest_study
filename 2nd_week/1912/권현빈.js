const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `5
-1 -2 -3 -4 -5
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = input();
const arr = input().split(" ").map(Number);

function solution() {
  let sum = 0;
  let answer = 0;

  if (arr.every((ele) => ele < 0)) {
    console.log(Math.max(...arr));
    return;
  }

  for (let i = 0; i < N; i++) {
    sum += arr[i];
    answer = Math.max(answer, sum);
    if (sum < 0) {
      sum = 0;
    }
  }
  console.log(answer);
}
solution();
