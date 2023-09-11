#!/usr/bin/node
const length = process.argv.length;
if (length < 4) {
  console.log(0);
} else {
  const myList = [];
  for (let i = 0; i < length - 2; i++) {
    myList[i] = Number(process.argv[i + 2]);
  }
  myList.sort();
  myList.reverse();
  console.log(myList[1]);
}
