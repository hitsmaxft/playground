var Ob = function(){

}

var events  = require('events')

Ob.prototype = new events.EventEmitter

var ob = new Ob()

var parser = function(callback, detail) {
    callback(detail+ "|" + detail)
}
var reacher = function(more_detail) {
    console.log(more_detail)
}
var cb = _.partial(parser, reacher)

ob.on("on", cb)
ob.emit("on", "a")
