#!/usr/bin/node
// Display the status code of a GET request.

const request = require('request');
const url = process.argv[2]
request.get(url, function (_error, response) {
  const todo = JSON.parse(response.body);
  const complete = []
  todo.forEach((s) => s.completed === true ? complete.push(s) : 0);
  const dict1 = {};
  let i = 1;
  while (true) {
    const x = [];
    complete.forEach((s) => s.userId === i ? x.push(s) : 0);
    if (x.length !== 0) {
      dict1[i] = x.length;
    } else {
      break;
    }
    i++;
  }
  console.log(dict1);
});
