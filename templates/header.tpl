<!DOCTYPE html>
<html lang="en">

<head>
    <title>TraderMinder®</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="build/merged.min.css" rel="stylesheet">
    <script defer src="build/merged.min.js"></script>
    <script src="https://code.jquery.com/jquery-3.6.3.min.js"
        integrity="sha256-pvPw+upLPUjgMXY0G+8O0xUf+/Im1MZjXxxgOcBQBXU=" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Iosevka/6.0.0/iosevka/iosevka.min.css">
</head>

<body style="background-color:#212529!important;color:white;">
    <nav class="navbar navbar-dark bg-dark fixed-top">
        <div class="container-fluid">
            <a class="navbar-brand" onclick="ldtemplate('home')">TraderMinder®</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas"
                data-bs-target="#offcanvasDarkNavbar" aria-controls="offcanvasDarkNavbar">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="offcanvas offcanvas-end text-bg-dark" tabindex="-1" id="offcanvasDarkNavbar"
                aria-labelledby="offcanvasDarkNavbarLabel">
                <div class="offcanvas-header">
                    <h5 class="offcanvas-title" id="offcanvasDarkNavbarLabel">TraderMinder®</h5>
                    <button type="button" class="btn-close btn-close-white" data-bs-dismiss="offcanvas"
                        aria-label="Close"></button>
                </div>
                <div class="offcanvas-body">
                    <ul class="navbar-nav justify-content-end flex-grow-1 pe-3">
                        <form class="d-flex mt-3" role="search">
                            <input class="form-control bg-dark text-bg-dark me-2" type="search" placeholder="Search"
                                aria-label="Search">
                            <button class="btn btn-outline-dark text-bg-dark" type="submit">Search</button>
                        </form>
                        <li class="nav-item">
                            <a class="nav-link" aria-current="page" onclick="ldtemplate('home')">Home </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" onclick="ldtemplate('teachers')">Teachers</a>
                        </li>
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown"
                                aria-expanded="false"> Topics
                            </a>

                            <span onclick="ldtemplate('category', 'elliot')" class="badge rounded-pill text-bg-primary">Elliot Wave</span>
                            <span onclick="ldtemplate('category', 'fib')" class="badge rounded-pill text-bg-secondary">Fib</span>
                            <span onclick="ldtemplate('category', 'Orderflow')" class="badge rounded-pill text-bg-success">Orderflow</span>
                            <span onclick="ldtemplate('category', 'Price Action')" class="badge rounded-pill text-bg-danger">Price Action</span>
                        </li>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" onclick="ldmodal('chatbot', 'AI Trading Assistant 🤖')">AI Trading
                                Assistant 🤖</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Terms of Service</a>
                        </li>
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown"
                                aria-expanded="false">
                                <img src="./uploads/20230213_230518.jpg" alt="Chicago"
                                    style="height:25px!important;width:25px!important"> My
                                Account
                            </a>
                            <ul class="dropdown-menu dropdown-menu-dark">
                                <li><a class="dropdown-item" href="#">Account</a></li>
                                <li><a class="dropdown-item" href="#"><span class="badge text-bg-success">PRO</span> My
                                        membership</a>
                                </li>
                                <li><a class="dropdown-item" href="#">Settings</a></li>
                                <li>
                                    <hr class="dropdown-divider">
                                </li>
                                <li><a class="dropdown-item" href="#">Logout</a></li>
                            </ul>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
</nav>