#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ', response && response.statusCode);
  }
});
