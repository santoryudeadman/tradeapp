<?php
require __DIR__ . './../server/config/config.php';
if (isset($_POST['modal'])) {
    $model = [
    "modalname" => strip_tags($_POST['modalname']),
    "modalid" => strip_tags($_POST['modal'])
    ];
    echo $handlebars->render(strip_tags($_POST['modal']), $model);
}
if (isset($_POST['tpl'])) {
    if ($_POST['tpl'] == 'category') {
    $model = [
        "type" => strip_tags($_POST['name']),
        ];
    } else if ($_POST['tpl'] == 'profile') {
        $model = [
            "traderimg" => strip_tags($_POST['img']),
            "traderdesc" => strip_tags($_POST['description']),
            "tradername" => strip_tags($_POST['name'])
            ];
    }
    echo $handlebars->render($_POST['tpl'], $model);
}