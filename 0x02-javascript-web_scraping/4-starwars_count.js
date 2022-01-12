#!/usr/bin/node

const request = require('request');
let x = 0;

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const startreks = JSON.parse(body).results;
  for (let y = 0; y < startreks.length; y++) {
    for (let g = 0; g < startreks[y].characters.length; g++) {
      if (startreks[y].characters[g].includes('18')) {
        x++;
      }
    }
  }
  console.log(x);
});
