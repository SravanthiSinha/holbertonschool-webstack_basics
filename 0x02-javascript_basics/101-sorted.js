#!/usr/bin/node

var dict = require('./101-data').dict;

var newdict = Object.keys(dict).map(function (key) {
  return { key: key, value: dict[key] };
}).sort(function (a, b) {
  return a.value - b.value;
});
var groupBy = function (xs, key) {
  return xs.reduce(function (rv, x) {
    (rv[x[key]] = rv[x[key]] || []).push(x.key);
    return rv;
  }, {});
};
newdict = groupBy(newdict, 'value');
console.log(newdict);
