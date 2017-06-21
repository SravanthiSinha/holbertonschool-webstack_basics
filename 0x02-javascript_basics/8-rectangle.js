#!/usr/bin/node
exports.Rectangle = function Rectangle (w, h) {
  if (w == null || h == null || w <= 0 || h <= 0) {
    return this;
  } else {
    this.width = w;
    this.height = h;
  }
};
