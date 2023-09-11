#!/usr/bin/node
const num = Number(process.argv[2]);
let str = '';
if (isNaN(num)) {
  console.log('Missing size');
} else if (num > 0) {
  for (let x = 0; x < num; x++) {
    for (let i = 0; i < num; i++) {
      str += 'X';
    }
    if (x !== num - 1) {
      str += '\n';
    }
  }
  console.log(str);
}
