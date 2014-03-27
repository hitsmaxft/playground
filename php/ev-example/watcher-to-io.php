<?php
$fd = fopen(__DIR__ ."/test.log", "rb");
// Wait until STDIN is readable
$w = new EvIo($fd, Ev::READ, function ($watcher, $revents) {
 echo "STDIN is readable\n";
});

Ev::run();
