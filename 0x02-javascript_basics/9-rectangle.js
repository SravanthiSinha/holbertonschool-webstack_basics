#!/usr/bin/node
exports.Rectangle = function Rectangle (w, h) {
  if (w == null || h == null || w <= 0 || h <= 0) {
    return this;
  } else {
    this.width = w;
    this.height = h;
  }
  this.print = function () {
    for (let i = 0; i < this.height; i++) {
      let op = '';
      for (let j = 0; j < this.width; j++) {
        op = op + 'X';
      }
      console.log(op);
    }
  };
};
