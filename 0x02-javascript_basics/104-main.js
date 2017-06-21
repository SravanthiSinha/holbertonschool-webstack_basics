#!/usr/bin/node
const callMeMoby = require('./104-call_me_moby').callMeMoby;
callMeMoby(3, function () {
  console.log('C is fun');
});
