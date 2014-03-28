var _ = require("underscore")
var hello = function (msg) {
    return "hello " + msg
}

var new_hello = _.wrap(hello , function(func, input){
    return  "wrap= say : " + func(input) + "."
})

console.log(new_hello("john"))
var newer_hello = _.compose(function(msg){return "composer= with" + msg; }, hello)
console.log(newer_hello("john"))
