#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const list1 = list.map((e) => e * list.indexOf(e));
console.log(list1);
