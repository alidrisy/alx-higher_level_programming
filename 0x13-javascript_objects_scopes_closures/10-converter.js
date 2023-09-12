#!/usr/bin/node

exports.converter = function (base) {
  return function (num) {
    if (!isNaN(parseInt(num.toString(base)))) {
      return parseInt(num.toString(base));
    } else {
      return num.toString(base);
    }
  };
};
