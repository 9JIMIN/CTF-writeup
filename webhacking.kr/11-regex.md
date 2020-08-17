# 11. regex

```php+HTML
<?php
  include "../../config.php";
  if($_GET['view_source']) view_source();
?><html>
<head>
<title>Challenge 11</title>
<style type="text/css">
body { background:black; color:white; font-size:10pt; }
</style>
</head>
<body>
<center>
<br><br>
<?php
  $pat="/[1-3][a-f]{5}_.*$_SERVER[REMOTE_ADDR].*\tp\ta\ts\ts/";
  if(preg_match($pat,$_GET['val'])){
    solve(11);
  }
  else echo("<h2>Wrong</h2>");
  echo("<br><br>");
?>
<a href=./?view_source=1>view-source</a>
</center>
</body>
</html>
```

코드를 보면 pat 변수에 정규식을 저장한다. 

```php
$pat="/[1-3][a-f]{5}_.*$_SERVER[REMOTE_ADDR].*\tp\ta\ts\ts/";
```

`$_SERVER[REMOTE_ADDR]` 는 접속한 컴퓨터 IP 주소이다. 

처음부터 해석을 해보면, 

```php
[1-3] # 1 ~ 3 중에 하나
```

```php
[a-f] # a ~ f 중에 하나
```

```php
{5} # x{5}는 x를 5번 반복한 문자, 여기서는 a-f의 조합을 5번 반복한 것을 뜻함
```

```php
[1-3][a-f]{5}_ # 여기까지는 1-3숫자하나와 a-f문자 5개 그리고 마지막에 _인 문자열을 의미함. ex) 1abcde_
```

```php
.x # . 은 임의의 한 문자를 뜻함. ex) ax, bx 
*x # x를 0번 이상 반복.
\t # tab 부분을 의미함. \tp\ta\ts\ts 는 '	p	a	s	s'이다. 
```

tab은 url encode를 하면 %09가 된다. 

즉 완성하면, `1abcde_39.112.202.229%09p%09a%09s%09s`

```
https://webhacking.kr/challenge/code-2/?val=1abcde_39.112.202.229%09p%09a%09s%09s
```

> 정규표현식을 해석할 수 있는지를 보는 문제이다. 
> tab키의 URL encode같은 것도 알 수 있었음.