#!/usr/bin/node

const wumbo = process.argv[3];
const fs = require('fs');
fs.writeFile(process.argv[2], wumbo, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
