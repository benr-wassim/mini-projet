<?php
$color = $_POST['color'];
error_log("Color received: $color", 0);

if ($color == 'off') {
    exec('sudo -u www-data /usr/bin/python /var/www/html/palette.py 0 0 0');
    echo "eteindre";
}
else {
    exec('sudo -u www-data /usr/bin/python /var/www/html/palette.py 0 0 0');
     // Convertir la couleur hexadécimale en valeurs RGB
        list($r, $g, $b) = sscanf($color, "#%02x%02x%02x");

        // Exécuter le script Python avec les valeurs RGB
        exec("sudo -u www-data /usr/bin/python /var/www/html/palette.py $r $g $b");
        echo $r.' '.$g.' '.$b ;
}
?>
