#!/usr/bin/node

const x = 'X';
const argv = process.argv[2];
if (argv && parseInt(argv)) {
  for (let i = 0; i < argv; i++) {
    console.log(x.repeat(argv));
  }
} else {
  console.log('Missing size');
}
