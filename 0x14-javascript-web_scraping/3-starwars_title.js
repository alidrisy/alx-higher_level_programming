#!/usr/bin/node
// Display the status code of a GET request.

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request.get(url, function (_error, response) {
  console.log(JSON.parse(response.body).title);
});
