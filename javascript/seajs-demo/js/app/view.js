define(function(require,exports, module){
    var _ = require("_")
    var $ = require("$")

    function View(tpl) {
        this._tpl= _.template(tpl)
        this.content = {
            name: "list",
            counter: 0,
        }
        this._tplList = _.template(
            "<p>current count: <%- counter %></p>"
            )
    }

    module.exports = View

    View.prototype.makeTitle = function (vars) {
        return this._tpl(vars)
    }

    View.prototype.makeContent = function (vars) {
        return this._tplList(vars)
    }

    View.prototype.domInject = function (title, body) {
        var _b = $("#container")
        if ( !_b.length ) {
            _b = $("<div></div>")
            _b.attr('id' , "container")
            $("body").append(_b)
        };
        _b.html("")
        _b.append(title).append(body)
    }

    View.prototype.compose = function (vars) {
        this.content.counter += 1

        var _t = this.makeTitle(vars)
        var _c = this.makeContent(this.content)
        this.domInject(_t , _c)
    }
}) 
// vim:ft=javascript.seajs
