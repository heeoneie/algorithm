const fs = require("fs")
const input = fs.readFileSync("/dev/stdin").toString().split(' ').map(Number)

const [A, B] = [input[0], input[1]]

if (A > B) console.log('>')
else if (A == B) console.log("==")
else console.log('<')