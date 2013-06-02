define(function(require, exports) {
    exports.init = function () {
        var _A_ = require("$")
        seajs.log("::test jquery, document title is " + _A_(document).attr("title"))

        var _U_ = require("_")
        seajs.log("::test underscore: " + _U_.template("|<%-v%>|", {v:1}))
        

        var _B_ = require("backbone")
        seajs.log("::test backbone, version is " + _B_.VERSION)

        var _C = require("./app/controller")

        seajs.log("::test simple mvc")
        var c = new _C("demo_controller")
        c.init()
        c.render()
    }
})
