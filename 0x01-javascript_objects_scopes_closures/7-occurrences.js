#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const instance of list) {
    if (instance === searchElement) { count++; } //search element being the requested occurance being counted
  }
  return count;
};
