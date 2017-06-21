#!/usr/bin/node
var fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], 'utf8', function (err, contents) {
  if (err) {
    console.log(err);
  }
});
