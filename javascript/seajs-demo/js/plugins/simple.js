define(function(require, exports, module){
    var $ = require("$")
    var css_loaded = false

    exports.load = function () {
        $("#container h1").addClass("splugins_simple_title")
        if (!css_loaded) {
            css_loaded = true
        }
    }

    exports.unload = function () {
        $("#container h1").removeClass("splugins_simple_title")
    }
})

