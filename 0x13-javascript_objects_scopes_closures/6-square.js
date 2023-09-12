#!/usr/bin/node
const Square1 = require('./5-square');

module.exports = class Square extends Square1 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0, str; i < this.width; i++) {
      str = '';
      for (let x = 0; x < this.width; x++) {
        str += c;
      }
      console.log(str);
    }
  }
};
