var lines = require('fs').readFileSync('/dev/stdin', 'utf8').split('\n');
var a = Number(lines.shift()); 
var b = Number(lines.shift()); 
var x = a + b;

console.log(`X = ${x}`);