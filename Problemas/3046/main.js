var lines = require('fs').readFileSync('/dev/stdin', 'utf8').split('\n');
var N = Number(lines.shift()); 

console.log(((N + 1) * (N + 2)) / 2);