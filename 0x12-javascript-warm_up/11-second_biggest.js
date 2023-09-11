#!/usr/bin/node
const length = process.argv.length;
if (length < 4) {
  console.log(0);
} else {
  const myList = [];
  for (let i = 0; i < length; i++) {
    myList[i] = Number(process.argv[i + 2]);
  }
  myList.sort();
  console.log(myList[length - 4]);
}
