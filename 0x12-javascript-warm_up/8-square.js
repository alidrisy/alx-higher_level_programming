#!/usr/bin/node
let num = Number(process.argv[2]);
let str = '';
if (isNaN(num)) {
  console.log('Missing size');
} else {
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
