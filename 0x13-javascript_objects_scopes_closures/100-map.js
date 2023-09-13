#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const list1 = list.map((e, index) => e * index);
console.log(list1);
