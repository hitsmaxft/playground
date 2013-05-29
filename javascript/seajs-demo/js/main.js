define(function(require) {
    var _A_ = require("$")
    console.log(_A_("body").html())

    var _U_ = require("_")
    console.log(_U_.template("|<%-v%>|", {v:1}))

    var _B_ = require("backbone")
    console.log(_B_.Model)

    var __ = require("mymod")
    __.show()
})
