#!/usr/bin/node
let fs = require('fs');

let contents1 = fs.readFileSync(process.argv[2]).toString();
let contents2 = fs.readFileSync(process.argv[3]).toString();

let wstream = fs.createWriteStream(process.argv[4]);
wstream.write(contents1);
wstream.write(contents2);
wstream.end();
