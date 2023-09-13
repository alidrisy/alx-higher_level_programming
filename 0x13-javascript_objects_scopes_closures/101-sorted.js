#!/usr/bin/node
const dict = require('./101-data').dict;

function arr (dct, value) {
const list = [];
for (const [key] of Object.entries(dct)) {
  if (dct[key] === value) {
    list.push(key);
  }
}
return list;
};

const dict1 = {};
for (const [key, value] of Object.entries(dict)) {
  dict1[value] = arr(dict, value);
}
console.log(dict1);
