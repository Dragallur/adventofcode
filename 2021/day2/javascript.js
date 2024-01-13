const fs = require('fs');
const input = fs.readFileSync('input.txt', 'utf-8').split('\n');

var horizontal = 0
var depth = 0
var horizontal2 = 0
var depth2 = 0
var aim = 0

for (let i = 0; i < input.length; i++) {
    s = input[i].split(' ')
    if (s[0] == 'forward') {
        horizontal += Number(s[1])
        horizontal2 += Number(s[1])
        depth2 += aim * Number(s[1])
    } else if (s[0] == 'up') {
        depth -= Number(s[1])
        aim -= Number(s[1])
    } else if (s[0] == 'down') {
        depth += Number(s[1])
        aim += Number(s[1])
    }
}

console.log(horizontal*depth)
console.log(horizontal2*depth2)