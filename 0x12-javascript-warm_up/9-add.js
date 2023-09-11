#!/usr/bin/node
const num1 = Number(process.argv[2]);
const num2 = Number(process.argv[3]);
if (isNaN(num1) || isNaN(num2)) {
  console.log('NaN');
} else {
  console.log(num1 + num2);
}
