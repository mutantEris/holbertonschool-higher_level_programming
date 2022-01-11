#!/usr/bin/node

const request = require('request');
const sunfights = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(sunfights, (err, _res, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
