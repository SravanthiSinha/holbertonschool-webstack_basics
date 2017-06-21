#!/usr/bin/node
const S = require('./109-square').Square;

exports.Square = function Square (size) {
  S.call(this, size);
};

exports.Square.prototype.charPrint = function charPrint (c) {
  if (c === undefined) {
    c = 'X';
  }
  for (let i = 0; i < this.height; i++) {
    let op = '';
    for (let j = 0; j < this.width; j++) {
      op = op + c;
    }
    console.log(op);
  }
};
