#!/usr/bin/node
const length = process.argv.length;

if (length <= 3) {
  console.log(0);
} else {
  const myList = [];
  for (let i = 0; i < length - 2; i++) {
    myList[i] = parseInt(process.argv[i + 2]);
  }
  myList.sort();
  myList.reverse();
  console.log(myList[1]);
}
