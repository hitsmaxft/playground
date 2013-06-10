define(function(require, exports, module){

    var plugins = seajs.config['data']['splugins']
    exports.pluginList = plugins

    //get enabled plugins from config
    exports.getList =  function () {
        return plugins
    }
})

