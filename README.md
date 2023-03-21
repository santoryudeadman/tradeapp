# drakesapp
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
<br>
php -r "if (hash_file('sha384', 'composer-setup.php') === '55ce33d7678c5a611085589f1f3ddf8b3c52d662cd01d4ba75c0ee0459970c2200a51f492d557530c71c15d8dba01eae') { 
    <br>
    echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"<br>
php composer-setup.php<br>
php -r "unlink('composer-setup.php');"
