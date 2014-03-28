var _ = require("underscore")

var func = function(a,b) {
    console.log("a is " + a)
    console.log("b is " + b)
}

var newfunc = _.partial(func, "a")

newfunc("b")
