<?php

$log_file = "/var/log/system.log";

// Use 10 second update interval.
$w = new EvStat($log_file, 8, function ($w) use($log_file) {
    echo "$log_file changed\n";

    $attr = $w->attr();

    if ($attr['nlink']) {
        printf("Current size: %ld\n", $attr['size']);
        printf("Current atime: %ld\n", $attr['atime']);
        printf("Current mtime: %ld\n", $attr['mtime']);
    } else {
        fprintf(STDERR, "`messages` file is not there!");
        $w->stop();
    }
});

Ev::run();
