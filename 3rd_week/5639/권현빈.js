const fs = require("fs");
const stdin = (process.platform === "linux"
  ? fs.readFileSync("/dev/stdin").toString()
  : `50
30
24
5
28
45
98
52
60
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const arr = [];
while (true) {
  let ele = parseInt(input());
  if (ele) {
    arr.push(ele);
  } else {
    break;
  }
}

function solution() {
  const binarySearchTree = (sub) => {
    if (sub.length === 0) {
      return;
    }
    let root = sub.shift();
    let leftArr = [];
    let rightArr = [];
    for (let i = 0; i < sub.length; i++) {
      if (sub[i] < root) leftArr.push(sub[i]);
      else rightArr.push(sub[i]);
    }
    binarySearchTree(leftArr);
    binarySearchTree(rightArr);
    console.log(root);
  };
  binarySearchTree(arr);
}

solution();
