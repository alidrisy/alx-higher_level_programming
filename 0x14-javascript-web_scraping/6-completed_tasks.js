#!/usr/bin/node
// Display the status code of a GET request.

const request = require('request');
const url = process.argv[2] + '?completed=true';
request.get(url, function (_error, response) {
  const charecter = JSON.parse(response.body);
  const dict1 = {};
  let i = 1;
  while (true) {
    const x = [];
    charecter.forEach((s) => s.userId === i ? x.push(s) : 0);
    if (x.length !== 0) {
      dict1[i] = x.length;
    } else {
      break;
    }
    i++;
  }
  console.log(dict1);
});
