#!/usr/bin/node

exports.esrever = function (list) {
  for (let x = 0; x < list.length / 2; x++) {
    [list[x], list[list.length - x - 1]] = [list[list.length - 1 - x], list[x]];
  }
  return list;
};
