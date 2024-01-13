const fs = require('fs');

const input = fs.readFileSync('input.txt', 'utf8').split('\n');
input.forEach((num, index) => {
    input[index] = Number(num);
});

var count = 0;
const window_size = 1;
for (let i = 0; i <= input.length - window_size; i++) {
    var sum1 = 0;
    var sum2 = 0;
    for (let j = 0; j < window_size; j++) {
        sum1 += input[i+j];
        sum2 += input[i+j+1];
    }
    if (sum2 > sum1) {
        count++;
    }
}

console.log(count);
