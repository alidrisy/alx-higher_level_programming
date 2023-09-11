#!/usr/bin/node
const num = Number(process.argv[2]);
console.log(Factorial(num));

function Factorial (n) {
  if (n === 1) {
    return 1;
  } else if (n > 1) {
    return n * Factorial(n - 1);
  } else {
    return 1;
  }
}
