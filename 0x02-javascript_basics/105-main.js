#!/usr/bin/node
const addMeMaybe = require('./105-add_me_maybe').addMeMaybe;
addMeMaybe(4, function (nb) {
  console.log('New value: ' + nb);
});
