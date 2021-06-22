var lines = require('fs').readFileSync('/dev/stdin', 'utf8').split('\n');
var raio = parseFloat(lines.shift());
const pi = 3.14159;
var area = (raio * raio) * pi;

console.log(`A=${area.toFixed(4)}`);