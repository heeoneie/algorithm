const input = require('fs').readFileSync('/dev/stdin').toString().trim().split(' ').map(BigInt);
const ans = input[0] + input[1]
console.log(ans.toString());