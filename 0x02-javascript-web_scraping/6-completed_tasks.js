#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const list = JSON.parse(body);
    const toDidList = {};

    for (let x = 0; x < list.length; x++) {
      if (list[x].completed) {
        if (toDidList[list[x].user_id]) {
          toDidList[list[x].user_id]++;
        } else {
          toDidList[list[x].user_id] = 1;
        }
      }
    }
    console.log(toDidList);
  }
});
