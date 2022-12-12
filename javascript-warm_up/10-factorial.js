#!/usr/bin/node

function factorial (f) {
  if (!f) {
    return 1;
  }
  return f * factorial(f - 1);
}
console.log(factorial(process.argv[2]));
