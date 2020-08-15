# SQL injection with raw md5 hash

id, pw제출란이 있다. 
소스는 아래와 같다.

```php+HTML
<?php
  include "../../config.php";
  if($_GET['view_source']) view_source();
?><html>
<head>
<title>Challenge 51</title>
<style>
table{ color:lightgreen;}
</style>
</head>
<body bgcolor=black><br><br>
<font color=silver>
<center><h1>Admin page</h1></center>
</font>
<?php
  if($_POST['id'] && $_POST['pw']){
    $db = dbconnect();
    $input_id = addslashes($_POST['id']);
    $input_pw = md5($_POST['pw'],true);
    $result = mysqli_fetch_array(mysqli_query($db,"select id from chall51 where id='{$input_id}' and pw='{$input_pw}'"));
    if($result['id']) solve(51);
    if(!$result['id']) echo "<center><font color=green><h1>Wrong</h1></font></center>";
  }
?>
<br><br><br>
<form method=post>
<table border=0 align=center bgcolor=gray width=200 height=100>
<tr align=center><td>ID</td><td><input type=text name=id></td></tr>
<tr align=center><td>PW</td><td><input type=password name=pw></td></tr>
<tr><td colspan=2 align=center><input type=submit></td></tr>
</table>
<font color=silver>
<div align=right><br>.<br>.<br>.<br>.<br><a href=./?view_source=1>view-source</a></div>
</font>
</form>
</body>
</html>
```

id와 pw를 받는 부분을 보자.

```php
$input_id = addslashes($_POST['id']);
$input_pw = md5($_POST['pw'],true);
```

id에는 특수문자 이스케이프를 하고, 
pw에는 받을 값을 md5 로 암호화한다. 암호화할때, true옵션이 있으면, 바이너리값을 반환한다. 

쿼리문을 보자.

```php
$result = mysqli_fetch_array(mysqli_query($db,"select id from chall51 where id='{$input_id}' and pw='{$input_pw}'"));
if($result['id']) solve(51);
```

목표는 $result['id']가 true가 되는 것이다. $result는 즉, id가 1이 되면 된다. 

그런데 pw에 SQL구문을 넣자니, 쿼리문에 삽입되기전에 md5로 암호화가 된다. 
하지만, 바이너리 형태로 리턴이 될 경우, 삽입이 가능하다. 

왜냐하면, 만약에 암호화의 리턴값이 `' or'1` 를 의미하는 바이너리가 될 경우 실재 삽입된 쿼리에서 동작할 수 있기 때문이다. 
즉, 암호화된 값이 바이너리로 리턴되어 들어갔을때, 쿼리문이 바이너리로 읽는 과정에서 같이 읽혀버릴 수 있다는 것이다. 

물론, md5로 암호화된 내용이 바이너리로 되기 때문에 안전할 듯 하지만, md5는 거의 인코딩급으로 다 뚫려가는 해시알고리즘이라서, 
인터넷에 검색하면, `'||or'` 의 해시값을 나오게 하는 값을 금방 찾을 수 있다.

- [SQL injection with raw md5-hash](https://cvk.posthaven.com/sql-injection-with-raw-md5-hashes)

```
id=1
pw=129581926211651571912466741651878684928
```

> 받은 값을 암호화해서 이용할때는, 
> 암호화된 값이 쿼리문(목표값)이 되도록 삽입하는 방법.
>
> md5 알고리즘의 취약성으로 인해 특정 해시값을 만드는 인풋값을 쉽게 알아낼 수 있다. 