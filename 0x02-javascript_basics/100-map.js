#!/usr/bin/node
let list = require('./100-data').list;

let newlist = list.map(function (num, index) {
  return num * index;
});

console.log(list);
console.log(newlist);
