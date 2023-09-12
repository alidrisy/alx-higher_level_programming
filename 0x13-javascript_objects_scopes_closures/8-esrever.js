#!/usr/bin/node

exports.esrever = function (list) {
  let i = 0;
  const list1 = [];
  for (let x = list.length - 1; x >= 0; x--) {
    list1[i] = list[x];
    i++;
  }
  return list1;
};
