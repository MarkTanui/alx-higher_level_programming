#!/usr/bin/node
function add(a, b){
    a = parseInt(process.argv[2]);
    b = parseInt(process.argv[3]);
    let sum = a + b;

    return sum;
}
console.log(add());