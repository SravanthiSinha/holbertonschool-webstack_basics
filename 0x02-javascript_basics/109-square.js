#!/usr/bin/node
const Rectangle = require('./107-rectangle').Rectangle;
exports.Square = function Square (size) {
  Rectangle.call(this, size, size);
};
