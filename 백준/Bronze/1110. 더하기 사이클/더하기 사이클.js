const input = require('fs').readFileSync('/dev/stdin').toString().trim();

let n = Number(input);
let cnt = 0;
let sum;

while (true) {
    cnt++;
    sum = Math.floor(n/10) + (n%10);
    n = (n%10)*10 + (sum%10);
    if (n == input) {
        break;
    }
}

console.log(cnt);