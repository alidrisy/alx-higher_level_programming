#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (!(!w || !h || w === 0 || h === 0 || h < 0 || w < 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0, str; i < this.height; i++) {
      str = '';
      for (let x = 0; x < this.width; x++) {
        str += 'X';
      }
      console.log(str);
    }
  }
};
