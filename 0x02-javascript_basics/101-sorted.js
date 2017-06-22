#!/usr/bin/node
let dict = require('./101-data').dict;

let newdict = Object.keys(dict).map(function (key) {
  return { key: key, value: dict[key] };
}).sort(function (a, b) {
  return a.value - b.value;
});
let groupBy = function (xs, key) {
  return xs.reduce(function (rv, x) {
    (rv[x[key]] = rv[x[key]] || []).push(x.key);
    return rv;
  }, {});
};
newdict = groupBy(newdict, 'value');
console.log(newdict);
