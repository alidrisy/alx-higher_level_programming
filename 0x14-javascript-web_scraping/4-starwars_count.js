#!/usr/bin/node
// Display the status code of a GET request.

const request = require('request');
const url = process.argv[2];
let x = 0;
request.get(url, function (_error, response) {
  const charecter = JSON.parse(response.body).results;
  for (const i of charecter) {
    if (i.characters.find((s) => s.includes('/18/'))) {
      x++;
    }
  }
  console.log(x);
});
