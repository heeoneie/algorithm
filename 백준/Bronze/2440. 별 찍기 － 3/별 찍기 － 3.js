const input = require('fs').readFileSync('/dev/stdin').toString().trim();

const n = Number(input);

for (let i = n; i>=1; i--) {
    console.log('*'.repeat(i));
}