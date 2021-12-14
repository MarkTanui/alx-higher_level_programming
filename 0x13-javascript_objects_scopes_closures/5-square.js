#!/usr/bin/node
module.sxports = class Square extends require('./4-rectangle') {
  constructor (size) {
    super(size, size);
  }
};
