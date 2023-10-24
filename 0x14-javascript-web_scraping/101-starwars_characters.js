#!/usr/bin/node
// Display the status code of a GET request.

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request.get(url, function (_error, response) {
  const charecter = JSON.parse(response.body).characters;
  for (const ur of charecter) {
    request.get(ur, function (_error, response) {
      const person = JSON.parse(response.body);
      console.log(person.name);
    });
  }
});
