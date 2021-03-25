const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `3
26 40 83
49 60 57
13 89 99
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = input();
const R = [0];
const G = [0];
const B = [0];
const RGB = [];

for (let i = 0; i < N; i++) {
  const [a, b, c] = input().split(" ");
  R.push(parseInt(a));
  G.push(parseInt(b));
  B.push(parseInt(c));
}
RGB.push(R);
RGB.push(G);
RGB.push(B);

// RGB = [ [0, 26, 49, 13 ], [0, 40, 60, 89 ], [0, 83, 57, 99 ] ]
function solution() {
  const dp = [[0, 0, 0]];
  let temp = [];
  for (let i = 1; i <= N; i++) {
    temp.push(Math.min(dp[i - 1][1], dp[i - 1][2]) + RGB[0][i]);
    temp.push(Math.min(dp[i - 1][0], dp[i - 1][2]) + RGB[1][i]);
    temp.push(Math.min(dp[i - 1][0], dp[i - 1][1]) + RGB[2][i]);
    dp.push(temp);
    temp = [];
  }
  console.log(Math.min(...dp[N]));
}

solution();
