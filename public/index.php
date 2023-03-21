<?php
require __DIR__ . './../server/config/config.php';
echo $handlebars->render("meta", $model);
#render home 
echo '<script>document.addEventListener("DOMContentLoaded", function (event) {ldtemplate("home");})</script>';
