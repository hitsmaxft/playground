seajs.config({
    debug:true,
    plugins: ['shim'],
    alias: {
        '$':'jquery/jquery/1.9.1/jquery-debug.js'
        , "_":'gallery/underscore/1.4.4/underscore-debug.js'
        , "backbone":'gallery/backbone/1.0.0/backbone-debug.js'
        , 'plugin-simple':'./plugins/simple'
    }
    , splugins: [
        'simple'
        , 'simple2'
    ]
});
