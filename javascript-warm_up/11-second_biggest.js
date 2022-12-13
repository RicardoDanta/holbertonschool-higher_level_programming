#!/usr/bin/node

function secondBiggest (arr) {
  if (arr.length < 2) {
    return 0;
  }
  arr.sort(function (a, b) {
    return a - b;
  });
  return arr[arr.length - 2];
}
console.log(secondBiggest(process.argv.slice(2)));
