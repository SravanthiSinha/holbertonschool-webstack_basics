#!/usr/bin/node
var fs = require('fs');

var contents1 = fs.readFileSync(process.argv[2]).toString();
var contents2 = fs.readFileSync(process.argv[3]).toString();

var wstream = fs.createWriteStream(process.argv[4]);
wstream.write(contents1);
wstream.write(contents2);
wstream.end();
