<?php
namespace Sample\Client;

require(dirname(__DIR__) . "/vendor/autoload.php");

use \EBernhardson\FastCGI\Client as FClient;

$client = new FClient('/usr/local/var/run/php54-fpm.sock');

$environment = [
    'REQUEST_METHOD'  => 'GET',
    'SCRIPT_FILENAME' => '/Volumes/SourceCode/playground/php/example-fastcgi-client/client/echo.php',
    ];

try {
    //$client->request($environment, $stdin);
    $client->request($environment, '');
    $rsp = $client->response();
    var_dump($rsp);
} catch (\EBernhardson\FastCGI\CommunicationException $failure) {
    echo "Error";
}


