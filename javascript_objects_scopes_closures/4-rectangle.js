#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const x = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(x.repeat(this.width));
    }
  }

  rotate () {
    const i = this.width;
    this.width = this.height;
    this.height = i;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
