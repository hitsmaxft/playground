define(function(require, exports, module){

    var plugins = seajs.config['data']['splugins']
    exports.pluginList = plugins
    exports.getList =  function () {
        return plugins
    }
})

