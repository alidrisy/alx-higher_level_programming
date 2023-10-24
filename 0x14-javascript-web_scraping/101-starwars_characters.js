#!/usr/bin/node
// Display the status code of a GET request.

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

function requestChar (characters, num) {
  if (num >= characters.length) {
    return;
  }
  request.get(characters[num], function (_error, _response, body) {
    console.log(JSON.parse(body).name);
    requestChar(characters, num + 1);
  });
}

request.get(url, function (_error, _response, body) {
  const characters = JSON.parse(body).characters;
  requestChar(characters, 0);
});
