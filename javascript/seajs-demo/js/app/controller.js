//simple controller
define(function(require,exports, module){
    var view = require("./view")
    var _ = require("_")
    var $ = require("$")
    var pm = require("./pluginman")

    require("./plugins/common.css")

    //factory for plugin dynamical loading
    //makes callback for lazy loading
    var load_plugins = function (name) {
        seajs.use( "/js/app/plugins/" + name
            , function (m) {
                var _v = document.getElementById("SPluginModule_"+name)
                if (!m) {
                    console.log("error on loading plugin " + name)
                    _v.checked = false
                    $(_v).parent().addClass("splugins_load_error")
                    return false
                }
                if ( _v.checked ){
                    m.load()
                    $(_v).parent().addClass("splugins_load_on")
                }else{
                    $(_v).parent().removeClass("splugins_load_on")
                    m.unload()
                }
            })
    }
    _v = new view("<h1>my name is <%- name%></h1>")

    function Controller(name) {
        this._v = _v
        this.name = name

    }
    module.exports = Controller

    Controller.prototype.render = function () {
        return this._v.compose(this)
    }

    var plugin_tpl = _.template("<li>"
            +"<input id=\"SPluginModule_<%= name%>\" "
            +" type=\"checkbox\" _name=\"<%=name%>\"/><label><%=name%>"
            +" </lable></li>"
        )
    //FIXME replace with event dispatching
    Controller.prototype.addPlugin = function (name) {
        seajs.log("add plugin:"+name)
        var script="seajs.require(\"" + name +"\")()"
        var element = $(plugin_tpl({"name":name})).attr( {"id":"SPlugin_"+name, "_name":name})
        $("#plugins .list").append(element)
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
        
        //init configured plugins
        _.each(pm.getList(), _.bind(function(i) {
                this.addPlugin(i)
            }, this))

        $("#plugins .list").on("change"
            , function(e) {
                seajs.log(e)
                var name = $(e.target).attr('_name')
                load_plugins(name)
            }
        )

        $("#plugins .submit").click(
            _.bind(function(e){
                var v = $(e.currentTarget).prev().val()
                console.log(v)
                this.addPlugin(v)
                }, this)
        )
    }
}) 
// vim:ft=javascript.seajs
