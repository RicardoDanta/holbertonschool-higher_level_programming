#!/usr/bin/node

exports.esrever = function (list) {
  const rlist = [];
  for (let i = 0; i < list.length; i++) {
    rlist.unshift(list[i]);
  }
  return rlist;
};
