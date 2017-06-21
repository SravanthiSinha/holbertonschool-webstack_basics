#!/usr/bin/node
var list = require('./100-data').list;

var newlist = list.map(function (num, index) {
  return num * index;
});

console.log(list);
console.log(newlist);
