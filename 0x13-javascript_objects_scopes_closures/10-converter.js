#!/usr/bin/node

exports.converter = function (base) {
  return function (num) {
    if (isNaN(parseInt(num.toString(base)))) {
      return num.toString(base);
    } else {
      return parseInt(num.toString(base));
    }
  };
};
