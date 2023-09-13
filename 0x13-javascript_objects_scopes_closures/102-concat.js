#!/usr/bin/node
const fs = require('fs');
const input = fs.readFileSync(process.argv[2], 'utf-8');
const input1 = fs.readFileSync(process.argv[3], 'utf-8');
fs.writeFileSync(process.argv[4], input + input1);
