#!/usr/bin/node
const length = process.argv.length;
let num;
if (length <= 3) {
  console.log(0);
} else {
  const myList = [];
  for (let i = 0; i < length - 2; i++) {
    myList[i] = parseInt(process.argv[i + 2]);
  }
  myList.sort((a, b) => a - b);
  myList.reverse();
  num = myList[1];
}
console.log(num);
