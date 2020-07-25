# 1- cookie
    <?php
    include "../../config.php";
    if($_GET['view-source'] == 1){ view_source(); }
    if(!$_COOKIE['user_lv']){
        SetCookie("user_lv","1",time()+86400*30,"/challenge/web-01/");
        echo("<meta http-equiv=refresh content=0>");
    }
    ?>
    <html>
    <head>
    <title>Challenge 1</title>
    </head>
    <body bgcolor=black>
    <center>
    <br><br><br><br><br>
    <font color=white>
    ---------------------<br>
    <?php
    if(!is_numeric($_COOKIE['user_lv'])) $_COOKIE['user_lv']=1;
    if($_COOKIE['user_lv']>=6) $_COOKIE['user_lv']=1;
    if($_COOKIE['user_lv']>5) solve(1);
    echo "<br>level : {$_COOKIE['user_lv']}";
    ?>
    <br>
    <a href=./?view-source=1>view-source</a>
    </body>
    </html>

- 끝에 쿠키값에 따라서 다른 결과를 보여준다. 
- user_lv쿠키값 >=6 이면 그냥 패스, > 5 면 solve.

solve를 위한 쿠키값은 5와 6사이에 있는 값이다.
쿠키값을 5.2로 편집하면 해결된다. 

>쿠키를 조작할 수 있는지를 보는 문제