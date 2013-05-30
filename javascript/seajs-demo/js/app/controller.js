//simple controller
define(function(require,exports, module){
    var view = require("./view")
    var _ = require("_")
    var $ = require("$")
    
    

    _v = new view("<h1>my name is <%- name%></h1>")

    function Controller(name) {
        this._v = _v
        this.name = name

    }
    module.exports = Controller

    Controller.prototype.render = function () {
        return this._v.compose(this)
    }

    Controller.prototype.init = function () {
        var button = $("<button>")
        button.html("render")
        button.click(
                _.bind(
                    function(){
                        seajs.log("trigger rendering");
                        this.render();
                    }
                    , this
                    )
                );
        $("body").append(button);
    }
}) 
// vim:ft=javascript.seajs
