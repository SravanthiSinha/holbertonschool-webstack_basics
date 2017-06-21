#!/usr/bin/node
if (process.argv.length <= 2) {
  console.log(0);
} else if (process.argv.length === 3) {
  console.log(0);
} else if (process.argv.length > 3) {
  console.log(process.argv.slice(2, process.argv.length).sort(function (a, b) {
    return b - a;
  })[1]);
}
