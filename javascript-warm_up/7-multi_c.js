#!/usr/bin/node

const c = 'C is fun';
const argv = process.argv;
if (!argv[2]) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < argv[2]; i++) { console.log(c); }
}
