const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `2 162
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let [A, B] = input().split(" ");
B = Number(B);
function solution() {
  const arr = [];
  const rec = (num, ans) => {
    let multiply = Number(num) * 2;
    let addOne = parseInt(num + "1");
    if (multiply === B || addOne === B) {
      arr.push(ans);
      return;
    }
    if (multiply < B) {
      rec(multiply, ans + 1);
    }
    if (addOne < B) {
      rec(addOne, ans + 1);
    }
    return;
  };

  rec(A, 1);

  if (!arr.length) {
    console.log(-1);
    return;
  }
  console.log(Math.min(...arr) + 1);
}

solution();
