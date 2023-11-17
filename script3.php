<?php

if (isset($_POST['action'])) {
    $action = $_POST['action'];

    if ($action === 'allumer') {
        exec('sudo -u www-data python /var/www/html/led3.py 1');
    } elseif ($action === 'eteindre') {
        exec('sudo -u www-data python /var/www/html/led3.py 0');
    }
}

?>
