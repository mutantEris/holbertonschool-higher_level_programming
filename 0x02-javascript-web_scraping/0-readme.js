#!/usr/bin/node

const fs = require('fs');

fs.readfile(process.argv[2], 'utf-8', (err, contents) => {
  if (!err) {
    console.log(contents.toString());
  } else {
    console.log(err);
  }
});
