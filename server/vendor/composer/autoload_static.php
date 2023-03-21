<?php

// autoload_static.php @generated by Composer

namespace Composer\Autoload;

class ComposerStaticInit2f5dffc3b398e8686de3896517658210
{
    public static $prefixesPsr0 = array (
        'H' => 
        array (
            'Handlebars' => 
            array (
                0 => __DIR__ . '/..' . '/salesforce/handlebars-php/src',
            ),
        ),
    );

    public static $classMap = array (
        'Composer\\InstalledVersions' => __DIR__ . '/..' . '/composer/InstalledVersions.php',
    );

    public static function getInitializer(ClassLoader $loader)
    {
        return \Closure::bind(function () use ($loader) {
            $loader->prefixesPsr0 = ComposerStaticInit2f5dffc3b398e8686de3896517658210::$prefixesPsr0;
            $loader->classMap = ComposerStaticInit2f5dffc3b398e8686de3896517658210::$classMap;

        }, null, ClassLoader::class);
    }
}