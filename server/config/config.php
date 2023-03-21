<?php
require __DIR__ . './../vendor/autoload.php';
//axious convert
$_POST = json_decode(file_get_contents("php://input"), true);
use Handlebars\Handlebars;
use Handlebars\Loader\FilesystemLoader;
# Connect to the database
#$GLOBALS['conn'] = mysqli_connect( '127.0.0.1', 'root', 'local', 'traderminder' );
# Set the partials files
$partialsDir = array(
    __DIR__ . "/../../templates",
    __DIR__ . "/../../modals",
);
$partialsLoader = new FilesystemLoader(
    $partialsDir,
    [
        "extension" => "tpl"
    ]
);

# We'll use $handlebars throughout this the examples, assuming the will be all set this way
$handlebars = new Handlebars([
    "loader" => $partialsLoader,
    "partials_loader" => $partialsLoader
]);
